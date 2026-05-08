# IEC 61131-3 Quick Reference

A handy one-page cheat sheet for the standard.

## The Five Languages

| Language | Acronym | Style | Typical use |
|----------|---------|-------|-------------|
| Ladder Diagram | LD | Graphical (rungs) | Discrete logic, interlocks |
| Function Block Diagram | FBD | Graphical (blocks) | Process control, reusable functions |
| Instruction List | IL | Textual (low-level) | Legacy — deprecated in 2013 edition |
| Structured Text | ST | Textual (Pascal-like) | Math, loops, complex conditions |
| Sequential Function Chart | SFC | Graphical (steps) | Sequences, batch, recipes |

## Data Types

### Elementary

| Type | Bits | Range |
|------|------|-------|
| `BOOL` | 1 | TRUE / FALSE |
| `BYTE` | 8 | 0 to 255 |
| `WORD` | 16 | 0 to 65 535 |
| `DWORD` | 32 | 0 to 4 294 967 295 |
| `LWORD` | 64 | unsigned 64-bit |
| `SINT` | 8 | –128 to +127 |
| `INT` | 16 | –32 768 to +32 767 |
| `DINT` | 32 | –2.1B to +2.1B |
| `LINT` | 64 | signed 64-bit |
| `USINT`, `UINT`, `UDINT`, `ULINT` | unsigned variants | |
| `REAL` | 32 | IEEE 754 single |
| `LREAL` | 64 | IEEE 754 double |
| `TIME` | 32 | duration |
| `STRING` | variable | character string |

### Derived

- `ARRAY[1..10] OF INT` — array
- `STRUCT…END_STRUCT` — record
- User-defined types via `TYPE…END_TYPE`

## Program Organization Units (POUs)

| POU | Has memory? | Returns value? |
|-----|-------------|-----------------|
| PROGRAM | Yes | No (instance) |
| FUNCTION_BLOCK | Yes | No (instance) |
| FUNCTION | No | Yes (single value) |

## ST Operators (precedence high → low)

1. `()` parentheses
2. Function call, exponentiation `**`
3. `NOT`, unary `-`
4. `*`, `/`, `MOD`
5. `+`, `-`
6. `<`, `>`, `<=`, `>=`
7. `=`, `<>`
8. `AND`, `&`
9. `XOR`
10. `OR`

## ST Control Flow

```pascal
IF cond THEN ... ELSIF cond THEN ... ELSE ... END_IF;

CASE expr OF
    1: ...
    2, 3: ...
    ELSE ...
END_CASE;

FOR i := 1 TO 10 BY 1 DO ... END_FOR;

WHILE cond DO ... END_WHILE;

REPEAT ... UNTIL cond END_REPEAT;
```

## Standard Function Blocks

| Block | Purpose |
|-------|---------|
| `TON` | On-delay timer |
| `TOF` | Off-delay timer |
| `TP` | Pulse timer |
| `CTU` | Up counter |
| `CTD` | Down counter |
| `CTUD` | Up/down counter |
| `R_TRIG` | Rising-edge detector |
| `F_TRIG` | Falling-edge detector |
| `RS` | Reset-dominant flip-flop |
| `SR` | Set-dominant flip-flop |

## SFC Action Qualifiers

| Qualifier | Meaning |
|-----------|---------|
| `N` | Non-stored — active while step is active |
| `S` | Set — latches on |
| `R` | Reset |
| `L` | Time-limited |
| `D` | Time-delayed |
| `P` | Pulse — single scan |
| `SD` | Stored and time-delayed |
| `DS` | Delayed and stored |
| `SL` | Stored and time-limited |
