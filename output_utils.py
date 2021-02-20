from text_styles import TextStyles

def error(text: str):
	print(f"{TextStyles.RED}{TextStyles.BOLD}{text}{TextStyles.ENDC}")

def warning(text: str):
	print(f"{TextStyles.BOLD}{text}{TextStyles.ENDC}")

def success(text: str):
	print(f"{TextStyles.GREEN}{TextStyles.BOLD}{text}{TextStyles.ENDC}")