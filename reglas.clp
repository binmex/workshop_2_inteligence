; reglas.clp

(defrule recomendacion-si
    ?f <- (respuesta si)
    =>
    (assert (recomendacion 45% de tener diabetes consulte con su medico))
    (retract ?f)
)

(defrule recomendacion-no
    ?f <- (respuesta no)
    =>
    (assert (recomendacion cero Esta dentro de los niveles normales))
    (retract ?f)
)