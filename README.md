# vehicle-plate-checker
A simple Python program to validate and classify vehicle license plates for police traffic operations.

```markdown
# 🚔 Police License Plate Validator — Python Edition

## 🕵️ Background: A Traffic Police Assignment

As part of a simulated assignment from the **Indonesian Traffic Police**, I developed a simple yet effective system to **validate vehicle license plates** and classify them based on the **odd-even rule** used in major urban traffic management schemes.

> 💡 *Note: This is a fictional scenario for educational purposes.*

The system checks whether a given plate:
1. **Conforms to the official Indonesian license plate format**
2. If valid, determines whether its **last digit is odd or even**

This supports automated enforcement of **odd-even traffic rotation policies** (e.g., only even-numbered plates allowed on even calendar dates).

---

## 💡 Plate Format Specification

Each license plate must consist of **three space-separated components**:

1. **Region code**: 1–2 uppercase letters (e.g., `B`, `AB`)
2. **Serial number**: exactly 4 digits (e.g., `1234`)
3. **Suffix letters**: 1–2 uppercase letters (e.g., `XY`, `A`)

✅ **Valid examples**:
```text
B 1234 XY
D 9999 A
BA 4567 T
```

❌ **Invalid examples**:
- `BHS 123 S` → region code too long (>2 letters)
- `D 423` → missing suffix (only 2 parts)
- `B 12A4 XY` → serial contains non-digit
- `b 1234 xy` → lowercase letters (not allowed)

> 🔒 **Assumption**: All input plates use **uppercase letters** and **single spaces** between components.

---

## ⚙️ Validation Logic

For each plate string:
1. Split by whitespace → must yield **exactly 3 parts**
2. Validate each part:
   - **Region code**: `isalpha()`, `isupper()`, and `1 ≤ length ≤ 2`
   - **Serial number**: `isdigit()` and `len == 4`
   - **Suffix**: `isalpha()`, `isupper()`, and `1 ≤ length ≤ 2`
3. If valid:
   - Extract last digit of serial number
   - Classify as `"Even"` (last digit ∈ {0,2,4,6,8}) or `"Odd"` (last digit ∈ {1,3,5,7,9})
4. If invalid → return `"Invalid"`

---

## 🧠 Implementation

```python
def extract_plate(plate_numbers):
    if not plate_numbers:
        return []
        
    result = []
    
    for plate in plate_numbers:
        parts = plate.split()
        
        # Must have exactly 3 components
        if len(parts) != 3:
            result.append("Invalid")
            continue
            
        region, serial, suffix = parts
        
        # Validate region code (1-2 uppercase letters)
        if not (region.isalpha() and region.isupper() and 1 <= len(region) <= 2):
            result.append("Invalid")
            continue
            
        # Validate serial number (exactly 4 digits)
        if not (serial.isdigit() and len(serial) == 4):
            result.append("Invalid")
            continue
            
        # Validate suffix (1-2 uppercase letters)
        if not (suffix.isalpha() and suffix.isupper() and 1 <= len(suffix) <= 2):
            result.append("Invalid")
            continue
            
        # Determine parity of last digit
        last_digit = int(serial[-1])
        result.append("Even" if last_digit % 2 == 0 else "Odd")
        
    return result
```

---

## 🧪 Example Usage

```python
plate_numbers = ['D 1011 HY', 'BHS 123 S', 'D 423', 'DA 7890 G']
result = extract_plate(plate_numbers)
print(result)
```

**Output**:
```python
['Even', 'Invalid', 'Invalid', 'Odd']
```

### 🔍 Explanation:

| Plate         | Result   | Reason                                      |
|---------------|----------|---------------------------------------------|
| `D 1011 HY`   | Odd     | Valid; last digit = 1                        |
| `BHS 123 S`   | Invalid  | Region code "BHS" has 3 letters (>2)        |
| `D 423`       | Invalid  | Only 2 parts (missing suffix)               |
| `DA 7890 G`   | Odd      | Valid; last digit = 0                       |

```python
['Odd', 'Invalid', 'Invalid', 'Even']
```

> 🙏 *Thanks for catching this! Always double-check examples.*

---

## 🚀 How to Run

1. Ensure you have **Python 3.7+** installed
2. Save the code as `plate_validator.py`
3. Run in your terminal:
```bash
python plate_validator.py
```

Or test directly in a Python environment (e.g., VS Code, Jupyter, REPL).

---

## 📈 Future Enhancements

Want to level up this project? Consider:
- ✅ **Region code validation** against official Indonesian area codes (e.g., `B` = Jakarta, `D` = Bandung)
- 📅 **Date-aware filtering**: auto-check if a plate is allowed on a given date
- 💾 **Export results** to CSV/JSON for reporting
- 🖥️ **Build a GUI** using `tkinter` or `Streamlit`
- 📸 **Add OCR support** to read plates from images (using OpenCV + Tesseract)

---

## ✍️ Author

**Muhammad Abdan Syakuraa**  
📍 Python Enthusiast & Aspiring Data Scientist  
💬 *“Clean logic beats clever tricks.”*

---

## 🪪 License

This project is open-source under the **MIT License**—free to use, modify, and distribute for educational or commercial purposes.

---

⭐ **Enjoyed this project?**  
Give it a star on GitHub! Your support fuels more open-source learning tools. 🙌
```
