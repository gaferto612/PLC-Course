(*
   Lab 05 — Burner Start-Up Sequence
*)

(* Phase transitions *)
IF NOT EStop AND Phase <> 0 THEN
    Phase := 5;
ELSIF Phase = 0 AND Start AND EStop THEN
    Phase := 1;
ELSIF Phase = 1 AND T_Purge_Done THEN
    Phase := 2;
ELSIF Phase = 2 AND Flame_OK THEN
    Phase := 3;
ELSIF Phase = 2 AND T_TFI_Done AND NOT Flame_OK THEN
    Phase := 5;
ELSIF Phase = 3 AND NOT Flame_OK THEN
    Phase := 5;
ELSIF Phase = 3 AND Stop THEN
    Phase := 4;
ELSIF Phase = 4 AND T_PostPurge_Done THEN
    Phase := 0;
ELSIF Phase = 5 AND Reset THEN
    Phase := 0;
END_IF;

(* Outputs *)
Y_Fan := (Phase = 1) OR (Phase = 2) OR (Phase = 3) OR (Phase = 4);
Y_Pilot := (Phase = 2) OR (Phase = 3);
Y_Main := Phase = 3;
Y_Igniter := Phase = 2;
Alarm := Phase = 5;
