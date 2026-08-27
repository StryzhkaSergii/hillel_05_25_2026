import re

row = """Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked Tom
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;"""

print(row.startswith("Tom gave up"))
print(row.endswith("material;"))
print(row[row.find("artist"):])
print("Tom" in row)

text = "Order #127 successfully created"
text_failed = "Order #22754 closed"
pattern = r"Order #(\d+) successfully created"
assert re.match(pattern, text), f"Operation response doesn't match expected: {text}"
assert re.match(pattern, text_failed), f"Actual: {text_failed}, Operation response doesn't match expected {pattern}"

uuid_correct = "1b4e28ba-2fa1-11d2-88f5-00a0c91e6bf6"
uuid_wrong = "1b4e28ba-2fa1-11d2-88f5-00a0c91e6"
uuid_pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"

email_validation_pattern = r"^[\w.-]+@[\w-]+\.[\w-]+$"