print("===== LIE DETECTOR SYSTEM =====")

# Input Section
heart_rate = input("Enter heart rate (bpm): ")
blink_rate = input("Enter eye blink rate (per minute): ")
response_time = input("Enter response time (seconds): ")
voice_pitch = input("Enter voice pitch variation (1-10): ")
sweating = input("Enter sweating level (1-10): ")

valid = True

# Input Validation
if not heart_rate.isdigit():
    print("Invalid heart rate input!")
    valid = False
if not blink_rate.isdigit():
    print("Invalid blink rate input!")
    valid = False
if not response_time.isdigit():
    print("Invalid response time input!")
    valid = False
if not voice_pitch.isdigit():
    print("Invalid voice pitch input!")
    valid = False
if not sweating.isdigit():
    print("Invalid sweating input!")
    valid = False

# Convert if valid
if valid:
    heart_rate = int(heart_rate)
    blink_rate = int(blink_rate)
    response_time = int(response_time)
    voice_pitch = int(voice_pitch)
    sweating = int(sweating)

    # Boundary checks
    if heart_rate <= 0 or blink_rate <= 0 or response_time < 0:
        print("Values must be positive!")
    elif voice_pitch < 1 or voice_pitch > 10:
        print("Voice pitch must be between 1 and 10!")
    elif sweating < 1 or sweating > 10:
        print("Sweating must be between 1 and 10!")
    else:
        lie_score = 0
        explanation = ""

        # Condition 1
        if heart_rate > 100:
            lie_score += 2
            explanation += "- High heart rate detected\n"
        elif heart_rate < 60:
            lie_score += 1
            explanation += "- Unusually low heart rate\n"
        else:
            explanation += "- Normal heart rate\n"

        # Condition 2
        if blink_rate > 30:
            lie_score += 2
            explanation += "- Excessive blinking\n"
        elif blink_rate < 10:
            lie_score += 1
            explanation += "- Very low blinking\n"
        else:
            explanation += "- Normal blinking\n"

        # Condition 3 (Nested)
        if response_time > 5:
            lie_score += 2
            explanation += "- Slow response\n"
            if heart_rate > 100:
                lie_score += 1
                explanation += "  -> Combined stress response detected\n"
                if sweating > 7:
                    lie_score += 1
                    explanation += "  -> High sweating confirms stress\n"
        elif response_time < 2:
            explanation += "- Quick response\n"
        else:
            explanation += "- Moderate response time\n"

        # Condition 4
        if voice_pitch > 7:
            lie_score += 2
            explanation += "- High pitch variation\n"
        elif voice_pitch < 3:
            explanation += "- Stable voice\n"
        else:
            lie_score += 1
            explanation += "- Slight voice variation\n"

        # Condition 5
        if sweating > 7:
            lie_score += 2
            explanation += "- High sweating\n"
        elif sweating < 3:
            explanation += "- Low sweating\n"
        else:
            lie_score += 1
            explanation += "- Moderate sweating\n"

        # Additional Conditions
        if heart_rate > 100 and blink_rate > 30:
            lie_score += 2
            explanation += "- Strong physiological stress combo\n"

        if response_time > 5 and voice_pitch > 7:
            lie_score += 2
            explanation += "- Nervous speaking pattern\n"

        if sweating > 7 and blink_rate > 30:
            lie_score += 1
            explanation += "- Anxiety indicators present\n"

        if heart_rate < 60 and response_time < 2:
            lie_score -= 1
            explanation += "- Calm and quick response\n"

        if voice_pitch < 3 and sweating < 3:
            lie_score -= 1
            explanation += "- Relaxed state\n"

        # Final Decision (Nested)
        print("\n===== RESULT =====")
        if lie_score >= 8:
            if heart_rate > 100:
                if sweating > 7:
                    result = "HIGH PROBABILITY OF LYING"
                else:
                    result = "LIKELY LYING"
            else:
                result = "LIKELY LYING"
        elif lie_score >= 4:
            result = "SUSPICIOUS BEHAVIOR"
        else:
            result = "LIKELY TRUTHFUL"

        print("Lie Score:", lie_score)
        print("Conclusion:", result)

        print("\n===== EXPLANATION =====")
        print(explanation)

else:
    print("\nSystem terminated due to invalid inputs.")
