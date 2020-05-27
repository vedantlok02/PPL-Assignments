(defparameter *my_list* '(9 8 7 6 5)) ;declare a list

(defvar num (read))	; take input via (read)

(defun display_nth(list position) ;define a function
    (format t "~a numbered Item in the List = ~a ~%" num (nth (- position 1) list))
)

;here nth is a lisp function. 
;nth (num list)
;it gives num'th element of the list

(display_nth *my_list* num)	;call the function display_nth