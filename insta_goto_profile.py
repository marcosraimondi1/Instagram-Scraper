def goto_profile(insta_user, driver):
    path = f"https://www.instagram.com/{insta_user}"

    driver.get(path)