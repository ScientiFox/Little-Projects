;Firmware brain for the Meep Robot

;QTR sensor
; >1 indicates black
; 

;Motor Control
;6 - left back
;7 - left forward
;5 - right back
;4 - right forward
;

;b1 is the state variable for sensors
;

;Start with setup
goto setup

;Read the right front qtr
readQTR_RF:
	; >1 indicates black
	;set state
	b1 = 0
	;pin high
	high 10
	;wait to charge
	pause 10
	;read sensor pin
	input 10
	;loop until pin toggles from discharge
	do
		let b1 = b1 + 1
	loop while pinC.2 = 1
	return

;read the left front qtr sensor
readQTR_LF:	
	; >1 indicates black
	;same as prior except for pin
	b1 = 0
	high 8
	pause 10
	input 8
	do
		let b1 = b1 + 1
	loop while pinC.0 = 1
	return
	
;read both QTRs
read_QTRs:
	;sets binary with 2*LF+1*RF
	;read left front
	gosub readQTR_LF
	;set b2 state variable for BBR routine
	if b1<2 then let b2=2 else let b2=0 endif
	;read right
	gosub readQTR_RF
	;set modified state
	if b1<2 then let b2=b2+1 endif
	;load actual variable with b2 and finish
	let b1 = b2
	b2 = 0
	return

;No setup- just a standard form
setup:
	goto repeat

;main loop
repeat:
	;read qrt sensors
	gosub read_QTRs
	
	;debug
	;b1 2 1
	; 0 0 0
	; 1 0 1
	; 2 1 0
	; 3 1 1
	
	;Implement BBR line-following routine
	;6 - left back
	;7 - left forward
	;5 - right back
	;4 - right forward

	if b1 = 1 then 
		high 6
		low 7
		low 5
		high 4;left back
	else if b1 = 2 then
		high 7
		low 6
		low 4
		high 5;right black
	else
		high 7
		low 6
		high 4
		low 5
	endif
		
	;pause 50 ;optimal smoothness pause
	goto repeat

