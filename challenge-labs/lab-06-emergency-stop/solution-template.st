(*
   Lab 06 — Emergency Stop (Cat 1)
*)

IF State = 0 AND EStop_OK AND Reset AND Drive_AtZero THEN
    State := 1;
ELSIF State = 1 AND Start AND EStop_OK THEN
    State := 2;
ELSIF State = 2 AND NOT EStop_OK THEN
    State := 3;
ELSIF State = 3 AND (T_Decel_Done OR Drive_AtZero) THEN
    State := 0;
END_IF;

Drive_Run_Cmd := State = 2;
Drive_Stop_Cmd := State = 3;
Power_Permit := (State = 1) OR (State = 2) OR (State = 3);
Ready := State = 1;
