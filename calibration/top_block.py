#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
<<<<<<< HEAD
# Generated: Thu Apr 13 19:58:54 2017
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
=======
# Generated: Thu Feb 11 17:48:24 2016
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
>>>>>>> parent of bcfe838... fixing noisefig calc to match doug
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
<<<<<<< HEAD
=======
import sip
import sys
>>>>>>> parent of bcfe838... fixing noisefig calc to match doug
import time


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
<<<<<<< HEAD
        self.samp_rate = samp_rate = 1E6
        self.gain = gain = 0
        self.bandwidth = bandwidth = 1E6
=======
        self.bandwidth = bandwidth = 5E6
        self.antenna = antenna = 3.625E9
        self.samp_rate = samp_rate = 2*bandwidth
        self.gain = gain = 30
        self.f0 = f0 = antenna
        self.FFT_Size = FFT_Size = 1024
>>>>>>> parent of bcfe838... fixing noisefig calc to match doug

        ##################################################
        # Blocks
        ##################################################
<<<<<<< HEAD
=======
        self._bandwidth_range = Range(1E6, 50E6, 1, 5E6, 200)
        self._bandwidth_win = RangeWidget(self._bandwidth_range, self.set_bandwidth, "bandwidth", "counter_slider", float)
        self.top_grid_layout.addWidget(self._bandwidth_win, 0,1,1,1)
        self._antenna_options = (750E6, 3.625E9, )
        self._antenna_labels = ("Lower band", "Upper Band", )
        self._antenna_group_box = Qt.QGroupBox("antenna")
        self._antenna_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._antenna_button_group = variable_chooser_button_group()
        self._antenna_group_box.setLayout(self._antenna_box)
        for i, label in enumerate(self._antenna_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._antenna_box.addWidget(radio_button)
        	self._antenna_button_group.addButton(radio_button, i)
        self._antenna_callback = lambda i: Qt.QMetaObject.invokeMethod(self._antenna_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._antenna_options.index(i)))
        self._antenna_callback(self.antenna)
        self._antenna_button_group.buttonClicked[int].connect(
        	lambda i: self.set_antenna(self._antenna_options[i]))
        self.top_grid_layout.addWidget(self._antenna_group_box, 0,0,1,1)
        self._samp_rate_range = Range(2*bandwidth, 8*bandwidth, 1E6, 2*bandwidth, 200)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, "samp_rate", "counter_slider", float)
        self.top_grid_layout.addWidget(self._samp_rate_win, 1,1,1,1)
        self._gain_range = Range(0, 30, 1, 30, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, "gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain_win, 2,0,1,1)
        self._f0_range = Range(675E6, 3.75E9, 1E6, antenna, 200)
        self._f0_win = RangeWidget(self._f0_range, self.set_f0, "f0", "counter_slider", float)
        self.top_grid_layout.addWidget(self._f0_win, 1,0,1,1)
        self._FFT_Size_range = Range(512, 4096, 1, 1024, 200)
        self._FFT_Size_win = RangeWidget(self._FFT_Size_range, self.set_FFT_Size, "FFT_Size", "counter_slider", float)
        self.top_grid_layout.addWidget(self._FFT_Size_win, 2,1,1,1)
>>>>>>> parent of bcfe838... fixing noisefig calc to match doug
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
<<<<<<< HEAD
        self.uhd_usrp_source_1.set_center_freq(3.625E9, 0)
        self.uhd_usrp_source_1.set_gain(gain, 0)
        self.uhd_usrp_source_1.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_1.set_bandwidth(bandwidth, 0)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_gr_complex*1, 20)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, 100)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*1, "/home/odroid/Documents/2ndRF/calibration/Power", False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
=======
        self.uhd_usrp_source_1.set_center_freq(f0, 0)
        self.uhd_usrp_source_1.set_gain(gain, 0)
        self.uhd_usrp_source_1.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_1.set_bandwidth(bandwidth, 0)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 3,0,1,2)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
        	FFT_Size, #size
        	firdes.WIN_KAISER, #wintype
        	0, #fc
        	bandwidth, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.01)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 4,1,1,1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
>>>>>>> parent of bcfe838... fixing noisefig calc to match doug

        ##################################################
        # Connections
        ##################################################
<<<<<<< HEAD
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_nlog10_ff_0, 0))    
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_head_0, 0), (self.blocks_conjugate_cc_0, 0))    
        self.connect((self.blocks_head_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_file_sink_1, 0))    
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_head_0, 0))    
        self.connect((self.uhd_usrp_source_1, 0), (self.blocks_skiphead_0, 0))    
=======
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_freq_sink_x_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.uhd_usrp_source_1, 0), (self.blocks_complex_to_mag_squared_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.set_samp_rate(2*self.bandwidth)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.bandwidth)
        self.uhd_usrp_source_1.set_bandwidth(self.bandwidth, 0)

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna
        self._antenna_callback(self.antenna)
        self.set_f0(self.antenna)
>>>>>>> parent of bcfe838... fixing noisefig calc to match doug

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_1.set_gain(self.gain, 0)
        	

<<<<<<< HEAD
    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.uhd_usrp_source_1.set_bandwidth(self.bandwidth, 0)
=======
    def get_f0(self):
        return self.f0

    def set_f0(self, f0):
        self.f0 = f0
        self.uhd_usrp_source_1.set_center_freq(self.f0, 0)

    def get_FFT_Size(self):
        return self.FFT_Size

    def set_FFT_Size(self, FFT_Size):
        self.FFT_Size = FFT_Size
>>>>>>> parent of bcfe838... fixing noisefig calc to match doug


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
