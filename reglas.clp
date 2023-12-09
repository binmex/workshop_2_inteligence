; reglas.clp

(defrule recomendacion-si
    ?f <- (respuesta si)
    =>
    (assert (recomendacion senderismo))
    (retract ?f)
)

(defrule recomendacion-no
    ?f <- (respuesta no)
    =>
    (assert (recomendacion gimnasio))
    (retract ?f)
)
