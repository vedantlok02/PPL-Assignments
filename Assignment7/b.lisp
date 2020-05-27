(defvar num (read))		;input num via keyboard
(defun rec_fac( n )		; function for factorial using recursion
  (if (= n 0)
    	1
	(* n (rec_fac(- n 1)))))

(format t "Factorial of ~D using recursion = ~D~%" num (rec_fac num))

(defun no_rec_fac(n) 	; function for factorial without using recursion
  (loop for i from 1 to n
	with a = 1
	do(setf a (* a i))
	finally (return a)))

(format t "Factorial of ~D without using recursion = ~D~%" num (no_rec_fac num))