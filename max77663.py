#!/usr/bin/env python
#
#
# Copyright (C) Canonical, Inc 2012

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class MAX77663:

    # constants
    max77663_regs = {
        0x05:'MAX77663_REG_IRQ_TOP',
        0x06:'MAX77663_REG_LBT_IRQ',
        0x07:'MAX77663_REG_SD_IRQ',
        0x08:'MAX77663_REG_LDOX_IRQ',
        0x09:'MAX77663_REG_LDO8_IRQ',
        0x0A:'MAX77663_REG_GPIO_IRQ',
        0x0B:'MAX77663_REG_ONOFF_IRQ',
        0x0C:'MAX77663_REG_NVER',
        0x0D:'MAX77663_REG_IRQ_TOP_MASK',
        0x0E:'MAX77663_REG_LBT_IRQ_MASK',
        0x0F:'MAX77663_REG_SD_IRQ_MASK',
        0x10:'MAX77663_REG_LDOX_IRQ_MASK',
        0x11:'MAX77663_REG_LDO8_IRQ_MASK',
        0x12:'MAX77663_REG_ONOFF_IRQ_MASK',
        0x16:'MAX77663_REG_SD0', #', #0x16
        0x17:'MAX77663_REG_SD1', #', #0x17
        0x18:'MAX77663_REG_SD2', #', #0x18
        0x19:'MAX77663_REG_SD3', #', #0x19
        0x1A:'MAX77663_REG_SD4', #', #0x1A
        0x1B:'MAX77663_REG_DVSSD0', #', #0x1B
        0x1C:'MAX77663_REG_DVSSD1', #', #0x1C
        0x1D:'MAX77663_REG_SD0_CFG', #', #0x1D
        0x1E:'MAX77663_REG_SD1_CFG', #', #0x1E
        0x1F:'MAX77663_REG_SD2_CFG', #', #0x1F
        0x20:'MAX77663_REG_SD3_CFG', #', #0x20
        0x21:'MAX77663_REG_SD4_CFG', #', #0x21
        0x23:'MAX77663_REG_LDO0_CFG', #', #0x23
        0x24:'MAX77663_REG_LDO0_CFG2', #', #0x24
        0x25:'MAX77663_REG_LDO1_CFG', #', #0x25
        0x26:'MAX77663_REG_LDO1_CFG2', #', #0x26
        0x27:'MAX77663_REG_LDO2_CFG', #', #0x27
        0x28:'MAX77663_REG_LDO2_CFG2', #', #0x28
        0x29:'MAX77663_REG_LDO3_CFG', #', #0x29
        0x2A:'MAX77663_REG_LDO3_CFG2', #', #0x2A
        0x2B:'MAX77663_REG_LDO4_CFG', #', #0x2B
        0x2C:'MAX77663_REG_LDO4_CFG2', #', #0x2C
        0x2D:'MAX77663_REG_LDO5_CFG', #', #0x2D
        0x2E:'MAX77663_REG_LDO5_CFG2', #', #0x2E
        0x2F:'MAX77663_REG_LDO6_CFG', #', #0x2F
        0x30:'MAX77663_REG_LDO6_CFG2', #', #0x30
        0x31:'MAX77663_REG_LDO7_CFG', #', #0x31
        0x32:'MAX77663_REG_LDO7_CFG2', #', #0x32
        0x33:'MAX77663_REG_LDO8_CFG', #', #0x33
        0x34:'MAX77663_REG_LDO8_CFG2', #', #0x34
        0x35:'MAX77663_REG_LDO_CFG3', #', #0x35
        0x36:'MAX77663_REG_GPIO_CTRL0',
        0x37:'MAX77663_REG_GPIO_CTRL1',
        0x38:'MAX77663_REG_GPIO_CTRL2',
        0x39:'MAX77663_REG_GPIO_CTRL3',
        0x3A:'MAX77663_REG_GPIO_CTRL4',
        0x3B:'MAX77663_REG_GPIO_CTRL5',
        0x3C:'MAX77663_REG_GPIO_CTRL6',
        0x3D:'MAX77663_REG_GPIO_CTRL7',
        0x3E:'MAX77663_REG_GPIO_PU',
        0x3F:'MAX77663_REG_GPIO_PD',
        0x40:'MAX77663_REG_GPIO_ALT',
        0x41:'MAX77663_REG_ONOFF_CFG1',
        0x42:'MAX77663_REG_ONOFF_CFG2',
		0x43:'MAX77663_REG_FPS_CFG0',
		0x44:'MAX77663_REG_FPS_CFG1',
		0x45:'MAX77663_REG_FPS_CFG2',
		0x46:'MAX77663_REG_FPS_LDO0',
		0x47:'MAX77663_REG_FPS_LDO1',
		0x48:'MAX77663_REG_FPS_LDO2',
		0x49:'MAX77663_REG_FPS_LDO3',
		0x4A:'MAX77663_REG_FPS_LDO4',
		0x4B:'MAX77663_REG_FPS_LDO5',
		0x4C:'MAX77663_REG_FPS_LDO6',
		0x4D:'MAX77663_REG_FPS_LDO7',
		0x4E:'MAX77663_REG_FPS_LDO8',
		0x4F:'MAX77663_REG_FPS_SD0',
		0x50:'MAX77663_REG_FPS_SD1',
		0x51:'MAX77663_REG_FPS_SD2',
		0x52:'MAX77663_REG_FPS_SD3',
		0x53:'MAX77663_REG_FPS_SD4',
        0x5C:'MAX77663_REG_CHIP_IDENT4',
		0x5D:'MAX77663_REG_CID5'
}

    max77663_power_mode = {
        0:'DISABLE',
        1:'GLPM',
        2:'LPM',
        3:'NORMAL'
    }

    max77663_slew_rate = {
        0:'13.75',
        1:'27.5',
        2:'55',
        3:'100'
    }



# ================================================

    in_reg_transaction = False
    temp_register = None
    regname = None


    def dump_generic(self, data):
        print "0x%0.2x" % data
        return
        if data & 0x80:
            print "[0x80 = 1]",
        else:
            print "[0x80 = 0]",
        if data & 0x40:
            print "[0x40 = 1]",
        else:
            print "[0x40 = 0]",
        if data & 0x20:
            print "[0x20 = 1]",
        else:
            print "[0x20 = 0]",
        if data & 0x10:
            print "[0x10 = 1]",
        else:
            print "[0x10 = 0]",
        if data & 0x08:
            print "[0x08 = 1]",
        else:
            print "[0x08 = 0]",
        if data & 0x04:
            print "[0x04 = 1]",
        else:
            print "[0x04 = 0]",
        if data & 0x02:
            print "[0x02 = 1]",
        else:
            print "[0x02 = 0]",
        if data & 0x01:
            print "[0x01 = 1]",
        else:
            print "[0x01 = 0]",
        print
        return

    def dump_voltage(self, data, min, step):
        print "[uV = %d]" % ((data * step) + min),
        return

    def dump_sd_cfg(self, data):
        print "[Power mode = %s]" % (self.max77663_power_mode[(data & 0x30) >> 4]),
        print "[Slew rate = %s]" % (self.max77663_slew_rate[(data & 0xc0) >> 6]),
        if data & 0x04:
            print "[Forced PWM]",
        if data & 0x01:
            print "[Active-Discharge Mode]",
        return

    def dump_ldo_cfg(self, data, step):
        self.dump_voltage(data & 0x3f, 800000, step)
        print "[Power mode = %s]" % (self.max77663_power_mode[(data & 0xc0) >> 6]),
        return

    def finish_register_access(self, deltatime, rw, data):
        if rw == "Read":
            rwtext = "(R)"
        else:
            rwtext = "(W)"
        print "max77663 : %s %s, data = 0x%0.2x" % (self.regname.ljust(12), rwtext,data),
        if ((self.temp_register == 0x16) or (self.temp_register == 0x18) or (self.temp_register == 0x19) or (self.temp_register == 0x1a)): # SD0, SD2, SD3, SD4
            self.dump_voltage(data & 0xff, 600000, 12500)
        elif self.temp_register == 0x17: # SD1
            self.dump_voltage(data & 0x3f, 800000, 12500)
        elif (self.temp_register >= 0x1D) and (self.temp_register <= 0x21): # SDx_CFG
            self.dump_sd_cfg(data)
        elif self.temp_register == 0x23: # LDO0_CFG
            self.dump_ldo_cfg(data, 25000);
        elif self.temp_register == 0x25: # LDO1_CFG
            self.dump_ldo_cfg(data, 25000);
        elif self.temp_register == 0x27: # LDO2_CFG
            self.dump_ldo_cfg(data, 50000);
        elif self.temp_register == 0x29: # LDO3_CFG
            self.dump_ldo_cfg(data, 50000);
        elif self.temp_register == 0x2b: # LDO4_CFG
            self.dump_ldo_cfg(data, 50000);
        elif self.temp_register == 0x2d: # LDO5_CFG
            self.dump_ldo_cfg(data, 50000);
        elif self.temp_register == 0x2f: # LDO6_CFG
            self.dump_ldo_cfg(data, 50000);
        elif self.temp_register == 0x31: # LDO7_CFG
            self.dump_ldo_cfg(data, 50000);
        elif self.temp_register == 0x33: # LDO8_CFG
            self.dump_ldo_cfg(data, 50000);
        print

        self.in_reg_transaction = False
        return
    
    def process_transaction(self, deltatime, rw, data):
        if self.in_reg_transaction:
            self.finish_register_access(deltatime, rw, data)
        elif data in self.max77663_regs:
            # This is the first half of a register access
            self.regname = self.max77663_regs[data]
            self.in_reg_transaction = True
            #print "%s:" % self.regname,
            self.temp_register = data
        else:
            print "max77663: Unknown register address %d, skipping" % data
