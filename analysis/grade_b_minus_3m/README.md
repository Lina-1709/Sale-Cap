# Tỷ lệ BD Grade B- — 3 tháng gần nhất (T8, T9, T10 MTD)

**Nguồn:** `[Internal SC] Grade C monitoring` → sheet `[SC] Data raw C movement` (cột M-2 = T8, M-1 = T9, MTD = T10 chốt 15/10/2026). 333 dòng BD.
**File:** `grade_raw_T8_T10.csv` (đã bỏ email), `b_minus_rate.py` (script tính lại).

## Định nghĩa và giả định
- **Tỷ lệ B-** = số BD có grade B- ÷ số BD có grade hợp lệ (A+/A/B+/B/B-/C) trong tháng đó. Loại BD có grade "-" (MOB0, chưa xếp grade) và BD trống (chưa vào / đã nghỉ).
- **Region** suy ra từ tên team: HN*/North* → North; HCM*/BCI HCM → South. *(Giả định)*
- **Team / Segment** lấy theo team MTD (hoặc team cuối cùng nếu BD đã nghỉ). BD chuyển team trong kỳ bị tính vào team hiện tại. *(Giả định)*
- **T10 = MTD 15/10**, chưa phải số chốt tháng.
- Mỗi team chỉ có 10–14 BD, nên **1 BD ≈ 7–10 điểm %**. Đọc số theo team như tín hiệu, chưa đủ để kết luận.

## 1. Total
| | T8 | T9 | T10 MTD |
|---|---|---|---|
| Toàn bộ BD có grade | 22/231 = **9.5%** | 23/249 = **9.2%** | 25/243 = **10.3%** |
| Chỉ MOB3+ | 18/179 = 10.1% | 21/189 = 11.1% | 21/182 = 11.5% |

## 2. Region
| | T8 | T9 | T10 MTD |
|---|---|---|---|
| North | 17/143 = 11.9% | 13/150 = 8.7% | 11/146 = **7.5%** |
| South | 5/88 = 5.7% | 10/99 = 10.1% | 14/97 = **14.4%** |

## 3. Segment (theo Region × Segment)
| | T8 | T9 | T10 MTD |
|---|---|---|---|
| North-FS | 12% (n=74) | 7% (n=75) | **3%** (n=70) |
| North-SME | 12% (n=69) | 11% (n=75) | 12% (n=76) |
| South-SME | 6% (n=62) | 13% (n=62) | **18%** (n=65) |
| South-FS | 5% (n=22) | 6% (n=34) | 3% (n=29) — nhóm này 86–93% là C |
| BCI | 0/4 | 0/3 | 1/3 |

Tổng theo Segment: FS 10.4% → 6.4% → 3.0%; SME 9.2% → 11.7% → 14.9%.

## 4. Team (tất cả BD có grade)
| Team | T8 | T9 | T10 MTD |
|---|---|---|---|
| HCM1 | 1/15 | 3/14 | 2/14 |
| HCM2 | 1/13 | 2/12 | 2/14 |
| HCM3 | 0/12 | 1/13 | **3/14** |
| HCM4 | 2/11 | 2/11 | 1/11 |
| HCM5 | 0/11 | 0/12 | **4/12** |
| HCM-F1 | 1/22 | 2/34 | 1/29 |
| BCI HCM | 0/4 | 0/3 | 1/3 |
| HN1 | 2/13 | 1/13 | 2/13 |
| HN2 | 2/10 | 2/10 | 0/11 |
| HN3 | 1/12 | 2/13 | 2/14 |
| HN4 | 0/10 | 1/12 | 1/11 |
| HN5 | 1/12 | 1/13 | 2/13 |
| HN6 | 2/12 | 1/14 | 2/14 |
| HN-F1 | 0/2 | 0/5 | 0/4 |
| HN-F2 | **3/10** | 0/9 | 1/13 |
| HN-F3 | 0/13 | 1/11 | 0/11 |
| HN-F4 | 2/13 | 2/13 | 0/12 |
| HN-F5 | 1/12 | 1/12 | 0/8 |
| HN-F6 | 0/11 | 0/12 | 0/9 |
| HN-FX | 1/7 | 1/7 | 1/7 |
| North-F1 | 2/6 | 0/6 | 0/6 |

## 5. Dịch chuyển (BD đi vào và đi ra khỏi B-)
| | B- T8 → T9 (n=22) | B- T9 → T10 MTD (n=23) |
|---|---|---|
| Lên grade (≥B) | 12 (55%) | 11 (48%) |
| Giữ B- | 7 (32%) | 5 (22%) |
| Rớt xuống C | 3 (14%) | **7 (30%)** |

**BD đi vào B- ở T10 (25 BD):** 15 BD (60%) rớt từ B trở lên (1 A+, 3 A, 5 B+, 6 B), 5 BD giữ B- từ T9, 4 BD đi lên từ C, 1 BD mới.
**Mắc kẹt B- cả 3 tháng:** 2 BD (HCM4-SME, HCM-F1-FS). Thêm 3 BD bị B- 2 tháng liên tiếp T9–T10 (HCM1 ×2, HN1).
