import time
import schedule
import httpx

print("this is a spatula project")

def main():
    text = "We've been trying to reach you about your car's extended warranty."
    httpx.post("https://ntfy.sh/very-very-annoying")
    print(f"Notificaton sent: {text} to https://ntfy.sh/very-very-annoying")
    data=text,
    headers={"Title": "Super important stuff, please read", "Tags": "rotating_light"}


if __name__ == "__main__":
    main()