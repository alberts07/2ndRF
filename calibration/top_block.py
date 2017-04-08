#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Apr  6 15:12:30 2017
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10E6
        self.gain = gain = 0
        self.f0 = f0 = 750E6
        self.bandwidth = bandwidth = 5E6
        self.antenna = antenna = 750E6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_center_freq(f0, 0)
        self.uhd_usrp_source_1.set_gain(gain, 0)
        self.uhd_usrp_source_1.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_1.set_bandwidth(bandwidth, 0)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, 100)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*1, "Power", False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_file_sink_1, 0))    
        self.connect((self.blocks_head_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.uhd_usrp_source_1, 0), (self.blocks_head_0, 0))    

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
        	

    def get_f0(self):
        return self.f0

    def set_f0(self, f0):
        self.f0 = f0
        self.uhd_usrp_source_1.set_center_freq(self.f0, 0)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.uhd_usrp_source_1.set_bandwidth(self.bandwidth, 0)

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
