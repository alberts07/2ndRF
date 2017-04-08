# File: ptfun
# Functions for gnuradio-companion PAM p(t) generation
import numpy as np

def pamhRt(sps, ptype, pparms=[]):
	"""
	PAM normalized matched filter (MF) receiver filter
	h_R(t) = h_R(n*TB/sps) generation
	>>>>> hRt = pamhRt(sps, ptype, pparms) <<<<<
	where sps:
		ptype: pulse type from list
			('man', 'rcf', 'rect', 'rrcf', 'sinc', 'tri')
		pparms not used for 'man', 'rect', 'tri'
		pparms = [k, alpha] for 'rcf', 'rrcf'
		pparms = [k, beta] for 'sinc'
		k: "tail" truncation parameter for 'rcf', 'rrcf', 'sinc'
			(truncates p(t) to -k*sps <=l n < k*sps)
		alpha: Rolloff parameter for 'rcf', 'rrcf', 0 <= alpha <= 1
		beta: Kaiser window parameter for 'sinc'
		hRt: MF impulse response h_R(t) at t=n*TB/sps
	Note: In terms of sampling rate Fs and baud rate FB,
		sps = Fs/FB
	"""
	if ptype.lower() == 'man':
		nn = np.arange(-sps/2, sps/2)
		# Need 1 then -1
		pt = np.ones(len(nn))


		ix = np.where(nn >= 0)[0]
		pt[ix] = -pt[ix]

		#ix1 = np.where(nn < len(nn) / 2)[0]
		#ix2 = np.where(nn >= len(nn) / 2)[0]
		#pt[ix1] = 1
		#pt[ix2] = -1
	elif ptype.lower() == 'rcf':

		nk = round(pparms[0] * sps)
		nn = np.arange(-nk, nk)
		pt = np.sinc(nn / float(sps))  # sinc pulse
		if len(pparms) > 1:
			p2t = 0.25 * np.pi * np.ones(len(nn))
			ix = np.where(np.power(2 * pparms[1] * nn / float(sps), 2.0) != 1)[0]
			p2t[ix] = np.cos(np.pi * pparms[1] * nn[ix] / float(sps))
			p2t[ix] = p2t[ix] / (1 - np.power(2 * pparms[1] * nn[ix] / float(sps), 2.0))
			pt = pt * p2t

	elif ptype.lower() == 'rect':

		nn = np.arange(-sps/2,sps/2)
		pt = np.ones(len(nn))

	elif ptype.lower() == 'rrcf':

		nk = round(pparms[0] * sps)
		nn = np.arange(-nk, nk)
		pt = np.zeros(len(nn))
		ix1 = np.where(nn == 0)[0]
		ix2 = np.where(np.logical_or(nn == -sps / (4 * pparms[1]), nn == sps / (4 * pparms[1])))[0]
		ix3 = np.where(np.logical_and(np.logical_and(nn != -sps / (4 * pparms[1]), nn != sps / (4 * pparms[1])), nn != 0))[0]
		pt[ix1] = 1 - pparms[1] + 4 * pparms[1] / np.pi
		pt[ix2] = pparms[1] / np.sqrt(2) * (
		(1 + 2 / np.pi) * np.sin(np.pi / (4 * pparms[1])) + (1 - 2 / np.pi) * np.cos(np.pi / (4 * pparms[1])))
		pt[ix3] = (np.sin((1 - pparms[1]) * np.pi * nn[ix3] / float(sps)) + 4 * pparms[1] * nn[ix3] / float(
			sps) * np.cos(
			(1 + pparms[1]) * np.pi * nn[ix3] / float(sps))) / (
				  np.pi * (1 - (4 * pparms[1] * nn[ix3] / float(sps)) ** 2) * nn[ix3] / float(sps))

	elif ptype.lower() == 'sinc':

		nk = round(pparms[0] * sps)
		nn = np.arange(-nk, nk)
		pt = np.sinc(nn / float(sps))
		if len(pparms) > 1:
			pt = pt * np.kaiser(len(pt), pparms[1])

	elif ptype.lower() == 'tri':

		nn = np.arange(-sps, sps)
		pt = np.zeros(len(nn))
		ix = np.where(nn < 0)[0]
		pt[ix] = 1 + nn[ix] / float(sps)
		ix = np.where(nn >= 0)[0]
		pt[ix] = 1 - nn[ix] / float(sps)

	else:
		pt = np.ones(1)

	pt = pt/(np.sum(pt**2))
	return pt


def pampt(sps, ptype, pparms=[]):

	#Code used from ECEN4242 last semester	

	"""
	PAM pulse p(t) = p(n*TB/sps) generation
	>>>>> pt = pampt(sps, ptype, pparms) <<<<<
	where sps:
		ptype: pulse type ('man', 'rcf, 'rect', 'rrcf' 'sinc', 'tri')
		pparms not used for 'man', 'rect', 'tri'
		pparms = [k,alpha] for 'rcf', 'rrcf'
		pparms = [k, beta] for sinc
		k: "tail" truncation parameter for 'rcf', 'rrcf', 'sinc'
			(truncates p(t) to -k*sps <= n < k*sps)
		alpha: Rolloff parameter for 'rcf', 'rrcf', 0 <= alpha <= 1
		beta: Kaiser window parameter for 'sinc'
		pt: pulse p(t) at t=n*TB/sps
	Note: In terms of sampling rate Fs and baud rate FB,
		sps = Fs/FB
	"""
	if ptype.lower() == 'rcf':
		nk = round(pparms[0]*sps)
		nn = np.arange(-nk,nk)
		pt = np.sinc(nn/float(sps)) # sinc pulse
		if len(pparms) > 1:
			p2t = 0.25*np.pi*np.ones(len(nn))
			ix = np.where(np.power(2*pparms[1]*nn/float(sps),2.0) != 1)[0]
			p2t[ix] = np.cos(np.pi*pparms[1]*nn[ix]/float(sps))
			p2t[ix] = p2t[ix]/(1-np.power(2*pparms[1]*nn[ix]/float(sps),2.0))
			pt = pt*p2t
	elif ptype.lower() == 'rrcf':
		nk = round(pparms[0] * sps)
		nn = np.arange(-nk, nk)
		pt = np.zeros(len(nn))
		ix1 = np.where(nn == 0)[0]
		ix2 = np.where(np.logical_or(nn == -sps / (4 * pparms[1]), nn == sps / (4 * pparms[1])))[0]
		ix3 = np.where(np.logical_and(np.logical_and(nn != -sps / (4 * pparms[1]), nn != sps / (4 * pparms[1])), nn != 0))[0]
		pt[ix1] = 1 - pparms[1] + 4 * pparms[1] / np.pi
		pt[ix2] = pparms[1] / np.sqrt(2) * ((1 + 2 / np.pi) * np.sin(np.pi / (4 * pparms[1])) + (1 - 2 / np.pi) * np.cos(np.pi / (4 * pparms[1])))
		pt[ix3] = (np.sin((1 - pparms[1]) * np.pi * nn[ix3] /float(sps)) + 4 * pparms[1] * nn[ix3] / float(sps) * np.cos(
			(1 + pparms[1]) * np.pi * nn[ix3] / float(sps))) / (np.pi * (1 - (4 * pparms[1] * nn[ix3] / float(sps)) ** 2) * nn[ix3] / float(sps))



	elif ptype.lower() == 'rect':
		nn = np.arange(-sps/2,sps/2)
		pt = np.ones(len(nn))
	elif ptype.lower() == 'sinc':
		nk = round(pparms[0]*sps)
		nn = np.arange(-nk,nk)
		pt = np.sinc(nn/float(sps))
		if len(pparms) > 1:
			pt = pt*np.kaiser(len(pt),pparms[1])
	elif ptype.lower() == 'tri':
		nn = np.arange(-sps, sps)
		pt = np.zeros(len(nn))
		ix = np.where(nn < 0)[0]
		pt[ix] = 1 + nn[ix]/float(sps)
		ix = np.where(nn >= 0)[0]
		pt[ix] = 1 - nn[ix]/float(sps)
	elif ptype.lower() == 'man':
		nn = np.arange(-sps/2, sps/2)
		# Need 1 then -1
		pt = np.ones(len(nn))


		ix = np.where(nn < 0)[0]
		pt[ix] = -pt[ix]
		print("transmitter")
		print(nn)
		print(pt)
	else:
		pt = np.ones(1)
	return pt



