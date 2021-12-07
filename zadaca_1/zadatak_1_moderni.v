Set Implicit Arguments.
Require Import Setoid.
Require Import Omega.
Require Import List.
Import ListNotations.
Require Import Arith.
Import Coq.Bool.Bool.


Goal forall X Y,
negb (X && Y) || negb X && Y || negb X && negb Y =
negb (X && Y).
Proof.
intros x y. destruct x,y ; simpl ; reflexivity.
Qed.

Goal forall X Y Z,
negb( negb X && Y && negb Z) && negb (X && Y && Y)
&& (X && negb Y && negb Z) = (X && negb Y) && negb Z.
Proof.
intros x y z. destruct x,y,z ; simpl ; reflexivity.
Qed. 