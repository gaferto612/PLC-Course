(*
   Lab 03 — Tank Fill/Drain
   Save as solution.st
*)

(* Phase transitions *)
IF Stop OR NOT EStop THEN
    Phase := 0;
ELSIF Phase = 0 AND Start THEN
    Phase := 1;
ELSIF Phase = 1 AND Level_Pct >= 80 THEN
    Phase := 2;
ELSIF Phase = 2 AND Hold_Done THEN
    Phase := 3;
ELSIF Phase = 3 AND Level_Pct <= 10 THEN
    Phase := 0;
END_IF;

(* Outputs derived from phase *)
Inlet_Valve := Phase = 1;
Outlet_Valve := Phase = 3;
Hold_Timer_EN := Phase = 2;
Cycle_Active := Phase <> 0;
