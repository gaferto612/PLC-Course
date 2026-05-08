(*
   Lab 02 — Conveyor Sort by Height
   Save as solution.st before submitting.
*)

(* Inspection: tall box detected when both sensors active *)
Tall_Detected := Sensor_Low AND Sensor_High;

(* Shift on rising edge of Index_Pulse *)
IF Index_Pulse AND NOT Last_Index THEN
    Track_P4 := Track_P3;
    Track_P3 := Track_P2;
    Track_P2 := Track_P1;
    Track_P1 := Track_P0;
    Track_P0 := Tall_Detected;
END_IF;

Last_Index := Index_Pulse;

(* Reject when tall box reaches position 4 *)
Reject_Sol := Track_P4;

(* Safety: clear everything on E-stop *)
IF NOT EStop THEN
    Track_P0 := FALSE;
    Track_P1 := FALSE;
    Track_P2 := FALSE;
    Track_P3 := FALSE;
    Track_P4 := FALSE;
    Reject_Sol := FALSE;
END_IF;
