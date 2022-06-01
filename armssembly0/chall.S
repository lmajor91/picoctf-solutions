	.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #16	; zero out stack pointer
				;;; basically, switch w0 and w1
	str	w0, [sp, 12]	; store word from sp+12 into w0
	str	w1, [sp, 8]	; store word from sp+8 into w1
	ldr	w1, [sp, 12]	; load word from sp+12 into w1
	ldr	w0, [sp, 8]	; load word from sp+8 into w0
				
	cmp	w1, w0		; compare w0 to w1
	bls	.L2		; jle .L2
	ldr	w0, [sp, 12]	; load word from sp+12 into w0
	b	.L3		; go to .L3
.L2:
	ldr	w0, [sp, 8]	; load sp+8 into w0
.L3:
	add	sp, sp, 16	; add sp+16, putting the result into sp
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	;;; x for 64-bit numbers
	;;; w for 32-bit numbers

	;;; ---
	stp	x29, x30, [sp, -48]!	; store register pair

	;; x29 = argv[0]
	add	x29, sp, 0	; adds 0 and sp, putting the result in x29

	;; storing things in memory
	str	x19, [sp, 16]	; store x19 in sp+16 (64b)
	str	w0, [x29, 44]	; store w0 in x29+44 (32b)
	str	x1, [x29, 32]	; store x1 in x29+32 (64b)

	;; move x1 into x0
	ldr	x0, [x29, 32]	; load x29+32 into x0
	add	x0, x0, 8	; adding x0 and 8, putting the result in x0
	ldr	x0, [x0]	; load the address of x0 into x0
	bl	atoi		; ascii to integer

	mov	w19, w0		; move w0 into w19
	ldr	x0, [x29, 32]	; load x29+32 into x0
	add	x0, x0, 16	; adding x0 and 16, putting the result in x0
	ldr	x0, [x0]	; load the address of x0 into x0
	bl	atoi		; ascii to integer

	mov	w1, w0		; move w0 into w1
	mov	w0, w19		; move w19 into w0

	bl	func1		; where function is called

	;;; ---

	mov	w1, w0		; move w0 into w1
	adrp	x0, .LC0	; shifts page, x0 contains the value of .LC0
	add	x0, x0, :lo12:.LC0 ; adding x0 and :lo12:.LC0, putting the result in x0
	bl	printf		; prints out the flag

	mov	w0, 0		; move 0 into w0
	ldr	x19, [sp, 16]	; load sp+16 into x19
	ldp	x29, x30, [sp], 48 ; load pair of registers
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
