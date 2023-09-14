import pyautogui as pg
import time


class JsxTestHelper:

    @staticmethod
    def verify_jsx_script_failure(error_img_path: str, error_img_confidence: float,
                                  max_attempts: int = 5, attempt_delay_seconds: int = 3):
        attempt_count = 0
        while attempt_count < max_attempts:
            result_img = bool(pg.locateOnScreen(error_img_path, confidence=error_img_confidence))
            if result_img:
                # Test passed
                pg.press('enter')
                time.sleep(5)
                return True

            time.sleep(attempt_delay_seconds)
            attempt_count += 1

        if attempt_count == max_attempts:
            print("Max attempts reached. Test failed.")
            pg.press("enter")
            return False
