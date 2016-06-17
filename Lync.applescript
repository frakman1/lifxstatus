tell application "System Events"
	tell process "Microsoft Lync"
		--set visible to true
		set test to name of menu button 1 of window "Microsoft Lync"
		return test
	end tell
end tell	