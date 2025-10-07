from pyats.topology import loader

# load testbed
testbed = loader.load('react_ai_agent_cisco_ios_xe/testbed.yaml')
router = testbed.devices['RUTX14']

# connect WITHOUT init commands
router.connect(init_commands=[])

# execute OpenWrt commands
print(router.execute('cat /etc/openwrt_release'))
print(router.execute('uci get network.lan.ipaddr'))
print(router.execute('ip addr'))

# disconnect
router.disconnect()
