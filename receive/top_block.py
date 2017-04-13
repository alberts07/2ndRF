#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Apr 12 18:55:37 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 600E3
        self.gain = gain = 0
        self.ft = ft = 75E3
        self.fm = fm = 1000
        self.fc = fc = 3.625E9

        ##################################################
        # Blocks
        ##################################################
        self.low_pass_filter_0_1 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, fm*4, fm/2, firdes.WIN_HAMMING, 6.76))
        self._gain_range = Range(0, 30, 1, 0, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, "gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain_win, 4,0,1,1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, ft, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fm, 1, 0)
        self.Time_RX = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.Time_RX.set_update_time(0.10)
        self.Time_RX.set_y_axis(-1, 1)
        
        self.Time_RX.set_y_label("Amplitude", "")
        
        self.Time_RX.enable_tags(-1, True)
        self.Time_RX.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.Time_RX.enable_autoscale(False)
        self.Time_RX.enable_grid(False)
        self.Time_RX.enable_control_panel(False)
        
        if not True:
          self.Time_RX.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.Time_RX.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.Time_RX.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.Time_RX.set_line_label(i, labels[i])
            self.Time_RX.set_line_width(i, widths[i])
            self.Time_RX.set_line_color(i, colors[i])
            self.Time_RX.set_line_style(i, styles[i])
            self.Time_RX.set_line_marker(i, markers[i])
            self.Time_RX.set_line_alpha(i, alphas[i])
        
        self._Time_RX_win = sip.wrapinstance(self.Time_RX.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Time_RX_win, 3,0,1,1)
        self.Freq_RX = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.Freq_RX.set_update_time(0.10)
        self.Freq_RX.set_y_axis(-140, 10)
        self.Freq_RX.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.Freq_RX.enable_autoscale(False)
        self.Freq_RX.enable_grid(False)
        self.Freq_RX.set_fft_average(1.0)
        self.Freq_RX.enable_control_panel(False)
        
        if not True:
          self.Freq_RX.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.Freq_RX.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Freq_RX.set_line_label(i, "Data {0}".format(i))
            else:
                self.Freq_RX.set_line_label(i, labels[i])
            self.Freq_RX.set_line_width(i, widths[i])
            self.Freq_RX.set_line_color(i, colors[i])
            self.Freq_RX.set_line_alpha(i, alphas[i])
        
        self._Freq_RX_win = sip.wrapinstance(self.Freq_RX.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Freq_RX_win, 2,0,1,1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.low_pass_filter_0_1, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.Freq_RX, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.Time_RX, 0))    
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_float_to_complex_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.Freq_RX.set_frequency_range(0, self.samp_rate)
        self.Time_RX.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, self.fm*4, self.fm/2, firdes.WIN_HAMMING, 6.76))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_ft(self):
        return self.ft

    def set_ft(self, ft):
        self.ft = ft
        self.analog_sig_source_x_1.set_frequency(self.ft)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.analog_sig_source_x_0_0.set_frequency(self.fm)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, self.fm*4, self.fm/2, firdes.WIN_HAMMING, 6.76))

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
