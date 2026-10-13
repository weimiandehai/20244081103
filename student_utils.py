def parse_student(line):
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError("字段数量不是2（可能缺逗号或多余逗号）")
    name, score_str = parts
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩 '{score_str}' 不是合法的整数")
    if not 0 <= score <= 100:
        raise ValueError(f"成绩 {score} 不在 0~100 范围内")
    return {"name": name, "score": score}