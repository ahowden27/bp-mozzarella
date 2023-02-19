import openai
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/misterrobot/Documents/chromedriver"
chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(PATH)

driver.get("C:whatever/Flask/group_work/index.html")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@id='button']")))
prompt_ = driver.find_element(By.XPATH, "//button[@id='button']").text
print(prompt_)

openai.organization = "org-rHdbbV2MAyPY28iF7ayK1HpI"

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt_,
  temperature=0.7,
  max_tokens=256
)

print(response)

# print()
# print("Here are some " + typeOfThing + "s that are similar to " + nameOfThing + ": ")
# print(response["choices"][0]["text"][2:len(response["choices"][0]["text"])])
