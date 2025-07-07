;Standard Delay
symbol delay_time = 10

;Start routine
goto repeat

;Delay function
delay:
	;Loop by 10ms until delay reached
	b0 = 0
	do
		let b0 = b0 + 1
		pause 10
	loop while b0 < delay_time

	;Go back
	return

;Main function
repeat:
	;Set pin 4 high, wait, then low: blink
	HIGH 4
	gosub delay
	LOW 4
	gosub delay
	GOTO repeat
