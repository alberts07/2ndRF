#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Apr 18 14:39:59 2017
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
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
        self.samp_rate = samp_rate = 60E3
        self.gain = gain = 15
        self.fc_fine = fc_fine = 0
        self.fc = fc = 3.625E9
        self.fL = fL = 3E3
        self.USRP_samp_rate = USRP_samp_rate = 600E3

        ##################################################
        # Blocks
        ##################################################
        self._gain_range = Range(0, 30, 1, 15, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, "gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain_win, 0,1,1,1)
        self._fc_fine_range = Range(-1E4, 1E4, 1, 0, 200)
        self._fc_fine_win = RangeWidget(self._fc_fine_range, self.set_fc_fine, "fc_fine", "counter_slider", float)
        self.top_grid_layout.addWidget(self._fc_fine_win, 1,1,1,1)
        self._fc_options = (3.625E9, 3.45E9, 3.80E9, 3.49E9, )
        self._fc_labels = ("In Band", "Out of band, lower", "Out of band, higher", "Way out", )
        self._fc_tool_bar = Qt.QToolBar(self)
        self._fc_tool_bar.addWidget(Qt.QLabel("fc"+": "))
        self._fc_combo_box = Qt.QComboBox()
        self._fc_tool_bar.addWidget(self._fc_combo_box)
        for label in self._fc_labels: self._fc_combo_box.addItem(label)
        self._fc_callback = lambda i: Qt.QMetaObject.invokeMethod(self._fc_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._fc_options.index(i)))
        self._fc_callback(self.fc)
        self._fc_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_fc(self._fc_options[i]))
        self.top_grid_layout.addWidget(self._fc_tool_bar, 0,0,1,1)
        self._fL_range = Range(1.5E3, samp_rate/2, 10E2, 3E3, 200)
        self._fL_win = RangeWidget(self._fL_range, self.set_fL, "fL", "counter_slider", float)
        self.top_grid_layout.addWidget(self._fL_win, 1,0,1,1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(USRP_samp_rate)
        self.uhd_usrp_source_0.set_center_freq(fc, 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"After LP", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_2.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_2.disable_legend()
        
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
                    self.qtgui_time_sink_x_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_2_win, 2,0,1,1)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(10, firdes.low_pass(
        	1, samp_rate, fL, fL/2, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(USRP_samp_rate, analog.GR_COS_WAVE, fc_fine, 1, 0)
        self.Time_RX = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Rx Signal", #name
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
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Time_RX.set_line_label(i, "Data {0}".format(i))
            else:
                self.Time_RX.set_line_label(i, labels[i])
            self.Time_RX.set_line_width(i, widths[i])
            self.Time_RX.set_line_color(i, colors[i])
            self.Time_RX.set_line_style(i, styles[i])
            self.Time_RX.set_line_marker(i, markers[i])
            self.Time_RX.set_line_alpha(i, alphas[i])
        
        self._Time_RX_win = sip.wrapinstance(self.Time_RX.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Time_RX_win, 3,0,1,1)
        self.Freq_RX_0 = qtgui.freq_sink_c(
        	8192, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"PSD", #name
        	1 #number of inputs
        )
        self.Freq_RX_0.set_update_time(0.10)
        self.Freq_RX_0.set_y_axis(-140, 10)
        self.Freq_RX_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.Freq_RX_0.enable_autoscale(False)
        self.Freq_RX_0.enable_grid(False)
        self.Freq_RX_0.set_fft_average(1.0)
        self.Freq_RX_0.enable_control_panel(False)
        
        if not True:
          self.Freq_RX_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.Freq_RX_0.set_plot_pos_half(not True)
        
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
                self.Freq_RX_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.Freq_RX_0.set_line_label(i, labels[i])
            self.Freq_RX_0.set_line_width(i, widths[i])
            self.Freq_RX_0.set_line_color(i, colors[i])
            self.Freq_RX_0.set_line_alpha(i, alphas[i])
        
        self._Freq_RX_0_win = sip.wrapinstance(self.Freq_RX_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Freq_RX_0_win, 3,1,1,1)
        self.Freq_RX = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"After LP", #name
        	1 #number of inputs
        )
        self.Freq_RX.set_update_time(0.10)
        self.Freq_RX.set_y_axis(-140, 10)
        self.Freq_RX.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.Freq_RX.enable_autoscale(False)
        self.Freq_RX.enable_grid(False)
        self.Freq_RX.set_fft_average(0.1)
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
        self.top_grid_layout.addWidget(self._Freq_RX_win, 2,1,1,1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.Time_RX, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.Freq_RX_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.Freq_RX, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_time_sink_x_2, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_xx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.Freq_RX.set_frequency_range(0, self.samp_rate)
        self.Freq_RX_0.set_frequency_range(0, self.samp_rate)
        self.Time_RX.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.fL, self.fL/2, firdes.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0.set_gain(self.gain, 0)
        	

    def get_fc_fine(self):
        return self.fc_fine

    def set_fc_fine(self, fc_fine):
        self.fc_fine = fc_fine
        self.analog_sig_source_x_0.set_frequency(self.fc_fine)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self._fc_callback(self.fc)
        self.uhd_usrp_source_0.set_center_freq(self.fc, 0)

    def get_fL(self):
        return self.fL

    def set_fL(self, fL):
        self.fL = fL
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.fL, self.fL/2, firdes.WIN_HAMMING, 6.76))

    def get_USRP_samp_rate(self):
        return self.USRP_samp_rate

    def set_USRP_samp_rate(self, USRP_samp_rate):
        self.USRP_samp_rate = USRP_samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.USRP_samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.USRP_samp_rate)


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
