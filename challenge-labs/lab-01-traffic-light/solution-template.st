(*
   Lab 01 — Traffic Light Controller
   ─────────────────────────────────
   Save this file as solution.st (in the same folder) before submitting.

   Inputs:  Start, Stop, T_Green_Done, T_Yellow_Done
   Outputs: Sequence_Active, RedNS, YellowNS, GreenNS, RedEW, YellowEW, GreenEW, Phase

   Phase encoding:
     0 = Stopped
     1 = NS_GREEN
     2 = NS_YELLOW
     3 = EW_GREEN
     4 = EW_YELLOW
*)

(* ── Phase transitions ────────────────────────────────── *)

IF Stop THEN
    Phase := 0;
ELSIF Phase = 0 AND Start THEN
    Phase := 1;
ELSIF Phase = 1 AND T_Green_Done THEN
    Phase := 2;
ELSIF Phase = 2 AND T_Yellow_Done THEN
    Phase := 3;
ELSIF Phase = 3 AND T_Green_Done THEN
    Phase := 4;
ELSIF Phase = 4 AND T_Yellow_Done THEN
    Phase := 1;
END_IF;

(* ── Sequence flag ────────────────────────────────────── *)

Sequence_Active := Phase <> 0;

(* ── Lamp outputs ─────────────────────────────────────── *)
(* TODO: set the six lamp outputs based on Phase. *)
(* Be careful not to double-coil. Set each output exactly once. *)

GreenNS  := FALSE;
YellowNS := FALSE;
RedNS    := FALSE;
GreenEW  := FALSE;
YellowEW := FALSE;
RedEW    := FALSE;

IF Phase = 1 THEN
    (* TODO: NS green, EW red *)
ELSIF Phase = 2 THEN
    (* TODO: NS yellow, EW red *)
ELSIF Phase = 3 THEN
    (* TODO: NS red, EW green *)
ELSIF Phase = 4 THEN
    (* TODO: NS red, EW yellow *)
ELSE
    (* Phase 0 — all red *)
    RedNS := TRUE;
    RedEW := TRUE;
END_IF;
