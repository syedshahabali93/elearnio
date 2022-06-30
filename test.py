from base import *
from locators import *
from constants import *


try:
    launch_browser()
    load_url(base_url)
    capture_screenshot("browser-login-page.PNG")
    wait_and_find_element(login_email_input)
    wait_and_enter_text(login_email_input, username)
    wait_and_find_element(login_password_input)
    wait_and_enter_text(login_password_input, password)
    wait_and_find_element(login_button)
    wait_and_click("login_button", login_button)
    wait_and_find_element(my_trainings_show_all_button)
    capture_screenshot("browser-home-page.PNG")
    wait_and_click("my_trainings_show_all_button", my_trainings_show_all_button)
    wait_and_find_element(course_status_dropdown)
    wait_and_click("course_status_dropdown", course_status_dropdown)
    wait_and_find_element(course_status_completed_dropdown_option)
    wait_and_click("course_status_completed_dropdown_option", course_status_completed_dropdown_option)
    wait_and_find_element((By.XPATH, "//body")).send_keys(Keys.ESCAPE)
    time.sleep(1)
    wait_and_find_element(course_modal)
    wait_and_click("course_modal", course_modal)
    wait_for_element_invisible(loading_spinner)
    wait_and_find_element(interactive_video_start_button)
    wait_and_click("interactive_video_start_button", interactive_video_start_button)
    capture_screenshot("browser-video-page.PNG")

    wait_and_find_element(video_play_button1)
    wait_and_click("video_play_button1", video_play_button1)
    print("Video playback started")
    time.sleep(1)
    video_slider_button = wait_and_find_element(video_slider_button)
    drag_and_drop(video_slider_button, -11, 0)
    print("Video playback started from beginning")
    time.sleep(1)

    # while (is_element_present(video_play_button2)):
    #     print("Video playback is in progress")
    #     time.sleep(30)
    # else:
    #     print("Video playback has finished")

    capture_screenshot("browser-video-ended.PNG")
    close_browser()


except Exception as e:
    print(e)
    exeMsg=type(e).__name__ + " : " + str(e)
    print(e)
    print(exeMsg)
    capture_screenshot("ss1.PNG")
#    close_browser()
    raise e






