//R0 baza 
//R1 eksponent
//spremi u R2 

@R0
D = M
@baza
M = D

@R1
D=M 
@eksponent
M=D

@j
M = 1   // j postavi na jedinicu 
(Potenciranjes)
    @R1
    D = M

    @j
    D = M - D    // od eksponentaa oduzimaj j 

    @Potenciranjea
    D; JGE   

    @LoopS
    0; JMP   


(LoopS)
@i
M = 0
    (LoopStart)
        @R0
        D = M

        @i
        D = M - D  // od baze oduzimaj i 

        @Loopa
        D; JGE   // ako je  D>= 0 


        @baza 
        D = M

        @k
        M = M + D   

        @i
        M = M + 1

        @LoopStart
        0; JMP

    (Loopa)

    @k
    D = M

    @baza
    M = D

    @k
    M = 0

    @j
    M = M + 1

    @Potenciranjes
    0; JMP

(Potenciranjea)
@baza
D = M
@R2
M = D

(END)
@END
0; JMP
