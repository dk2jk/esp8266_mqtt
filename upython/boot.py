# This file is executed on every boot (including wake-boot from deepsleep)
import esp; esp.osdebug(None)
import  machine
import gc
gc.collect()

#anzeige der reset-ursache...
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('\nwoke from a deep sleep')
else:
    print('\npower on or hard reset')
