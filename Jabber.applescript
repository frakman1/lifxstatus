tell application "System Events"
	tell process "Cisco Jabber"
		--set visible to true
		set test to help of menu button 1 of window "Cisco Jabber"
		return test
	end tell
end tell