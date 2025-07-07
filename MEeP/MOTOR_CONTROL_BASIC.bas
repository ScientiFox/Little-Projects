;basic controller linear actuator test
;driving sn754410

;Set delay time and goto init routine
symbol delay_time = 35
goto setup

;Initialization
setup:
	;set pins 4 and 1 low
	low 4
	low 1
	;wait a moment, then goto main loop
	gosub delay
	goto repeat

;Main Loop
repeat:
	;set 4 high and wait - left turn
	high 4
	gosub delay

	;set 4 and 1 low and wait
	low 4
	low 1
	gosub delay

	;set 1 high- right turn
	high 1
	gosub delay
	
	;set both low
	low 1
	low 4
	gosub delay
	
	goto repeat

;subroutines
delay:
	;loop by 10ms until delay time reached
	b0 = 0
	do
		let b0 = b0 + 1
		pause 10
	loop while b0 < delay_time
	return
