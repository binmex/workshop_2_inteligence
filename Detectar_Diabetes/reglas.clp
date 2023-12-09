(defglobal ?*probabilidad* = 0.20)

(defrule edad-menor-40
    ?f <- (edad ?e&:(<= ?e 40))
    =>
    (bind ?*probabilidad* (+ ?*probabilidad* 0.15))
    (retract ?f)
)

(defrule edad-mayor-40
    ?f <- (edad ?e&:(> ?e 40))
    =>
    (bind ?*probabilidad* (+ ?*probabilidad* 0.30))
    (retract ?f)
)

(defrule glucosa-menor-127
    ?f <- (nivel-insulina ?e&:(<= ?e 127))
    =>
    (bind ?*probabilidad* (+ ?*probabilidad* 0.25))
    (retract ?f)
)

(defrule glucosa-mayor-127
    ?f <- (nivel-insulina ?e&:(> ?e 127))
    =>
    (bind ?*probabilidad* (+ ?*probabilidad* 0.35))
    (retract ?f)
)

(defrule imc-menor-25
    ?f <- (imc ?imc&:(<= ?imc 25))
    =>
    (bind ?*probabilidad* (+ ?*probabilidad* 0.17))
    (retract ?f)
)

(defrule imc-mayor-25
    ?f <- (imc ?imc&:(> ?imc 25))
    =>
    (bind ?*probabilidad* (+ ?*probabilidad* 0.27))
    (retract ?f)
)

(defrule calcular-probabilidad-total
    =>
    (assert (probabilidad-total ?*probabilidad*))
)

(defrule mostrar-probabilidad
    (probabilidad-total ?total&:(> ?total 0))
    =>
    (printout t "Probabilidad acumulativa de tener diabetes: " (* ?total 100) crlf)
    (reset)
    (bind ?*probabilidad* 0)
)




