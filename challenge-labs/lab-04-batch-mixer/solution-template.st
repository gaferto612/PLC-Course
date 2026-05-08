(*
   Lab 04 — Batch Mixer
*)

IF Stop OR NOT EStop THEN
    Phase := 0;
ELSIF Phase = 0 AND Start THEN
    Phase := 1;
ELSIF Phase = 1 AND Flow_Total >= 50 THEN
    Phase := 2;
ELSIF Phase = 2 AND Weight_Total >= 25 THEN
    Phase := 3;
ELSIF Phase = 3 AND Mix_Done THEN
    Phase := 4;
ELSIF Phase = 4 AND Tank_Empty THEN
    Phase := 0;
END_IF;

Y_Water := Phase = 1;
Y_Sugar := Phase = 2;
Mixer_Run := Phase = 3;
Y_Drain := Phase = 4;
