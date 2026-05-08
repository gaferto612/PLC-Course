# Manufacturer Mapping

Same concepts, different names. This table is your Rosetta Stone for moving between vendor documentation.

## Languages

| IEC 61131-3 | Siemens TIA Portal | Allen-Bradley Studio 5000 | Mitsubishi GX Works | CODESYS |
|-------------|--------------------|----------------------------|---------------------|---------|
| LD | KOP | Ladder Diagram | Ladder | LD |
| FBD | FUP | Function Block | Function Block | FBD |
| IL | AWL (S7-300/400 only) | (not supported) | Instruction List | IL (deprecated) |
| ST | SCL | Structured Text | Structured Text | ST |
| SFC | GRAPH | (no native equivalent — use Add-On Instructions) | SFC | SFC |

## I/O Addressing

### Discrete input on terminal 0 of card 1

| Vendor | Notation |
|--------|----------|
| Siemens (S7) | `I0.0`, `%I0.0` |
| Siemens (legacy) | `E0.0` (German: *Eingang*) |
| Allen-Bradley Logix | `Local:1:I.Data.0` |
| Allen-Bradley PLC-5/SLC-500 | `I:1/0` (octal!) |
| Mitsubishi FX/Q | `X0` (octal!) |
| Omron | `0.00` |
| CODESYS | `%IX0.0` |

### Discrete output

| Vendor | Notation |
|--------|----------|
| Siemens (S7) | `Q0.0`, `%Q0.0` |
| Siemens (legacy) | `A0.0` (German: *Ausgang*) |
| Allen-Bradley Logix | `Local:2:O.Data.0` |
| Allen-Bradley SLC | `O:2/0` |
| Mitsubishi | `Y0` |
| Omron | `100.00` |

### Internal flag (memory bit)

| Vendor | Notation |
|--------|----------|
| Siemens | `M0.0` (Merker) |
| Allen-Bradley SLC | `B3:0/0` |
| Allen-Bradley Logix | tag-based (any name) |
| Mitsubishi | `M0` |

### Analog input (16-bit word)

| Vendor | Notation |
|--------|----------|
| Siemens | `IW64`, `PIW64` |
| Allen-Bradley | `Local:3:I.Ch0Data` |
| Mitsubishi | `D100` |

## Memory Areas

| Vendor | Inputs | Outputs | Internal | Data | Constants |
|--------|--------|---------|----------|------|-----------|
| Siemens | I / E | Q / A | M | DB (Data Block) | — |
| Allen-Bradley SLC | I | O | B | N (integer), F (float) | — |
| Mitsubishi | X | Y | M | D | K (constants) |

## Common Function Block Naming

| Function | Siemens | Allen-Bradley | Mitsubishi |
|----------|---------|---------------|------------|
| On-delay timer | `TON` (LAD) / `S_ODT` | `TON` | `TIMER` (with K-preset) |
| Off-delay timer | `TOF` / `S_OFFDT` | `TOF` | (custom) |
| Up counter | `CTU` / `S_CU` | `CTU` | `COUNTER` |
| Move | `MOVE` | `MOV` | `MOV` |
| Add (integer) | `ADD_I` | `ADD` | `+` |
| Compare | `CMP` boxes | `EQ`, `LT`, `GT`, etc. | `=`, `<`, `>` |

## Programming Tools

| Vendor | Tool |
|--------|------|
| Siemens | TIA Portal (modern), STEP 7 (classic) |
| Allen-Bradley | Studio 5000 Logix Designer, RSLogix 500 (legacy) |
| Mitsubishi | GX Works2 / GX Works3 |
| Omron | Sysmac Studio |
| Schneider Electric | EcoStruxure Control Expert (Unity Pro), Machine Expert |
| ABB | Automation Builder |
| Beckhoff | TwinCAT |
| CODESYS-based vendors | CODESYS Development System |

## Bus Standards

| Bus | Siemens | Allen-Bradley | Other |
|-----|---------|---------------|-------|
| Industrial Ethernet | PROFINET | EtherNet/IP | EtherCAT (Beckhoff), POWERLINK |
| Fieldbus | PROFIBUS DP | DeviceNet, ControlNet | Modbus RTU, AS-i |
| Safety | PROFIsafe | CIP Safety | FSoE (Fail-Safe over EtherCAT) |

## Tip: Translation Strategy

When you encounter a new vendor:

1. Find their term for **input image table** and **output image table**.
2. Find their **internal bit / memory bit** notation.
3. Find their **timer instruction** and how presets are entered.
4. Find their **online monitoring** view.

These four anchors carry over the bulk of your IEC 61131-3 knowledge to any new platform.
