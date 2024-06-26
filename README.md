# Smart ATS

Smart ATS is an AI-powered tool designed to help HR recruiters efficiently review and evaluate candidates' resumes against job descriptions. It provides detailed analysis including the match percentage, missing keywords, profile summary, and highlights skills present or missing in the candidate's resume compared to the job description.

## Features

- **JD % Match**: Calculates how well the candidate's resume matches the job description.
- **Missing Keywords**: Identifies keywords that are present in the job description but missing in the resume.
- **Profile Summary**: Generates a concise summary of the candidate's profile.
- **Skills Analysis**: Compares the skills listed in the resume with those required by the job description and identifies any gaps.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tirth2212/Resume_Helper.git
    cd Resume_Helper
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY="your_openai_api_key"
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Paste the job description in the designated text area.

4. Upload the candidate's resume in PDF format.

5. Click the "Submit" button to get the evaluation results.

## Example

Here is an example of the expected output:
![Sample Output](https://github.com/tirth2212/Resume_Helper/blob/main/Sample%20Output.png)

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or feedback, please open an issue or contact me at tirthshah7@gmail.com

```

Feel free to customize this README file further based on your specific requirements or preferences.
```
