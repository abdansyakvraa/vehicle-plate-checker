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
