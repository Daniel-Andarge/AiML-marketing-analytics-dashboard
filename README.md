# Sentiment Analysis and Marketing Dashboard for Ethiopian Bank

This project focused on developing a comprehensive sentiment analysis and marketing dashboard solution for an Ethiopian bank. The goal was to provide the bank's marketing and sales teams with data-driven insights to optimize their campaigns and strategies.

### The key aspects of the project include:

- Sentiment Analysis:
Leveraging natural language processing (NLP) techniques to analyze customer feedback and comments from various channels, including the bank's mobile app, social media, and customer support interactions. This helped identify emerging sentiment trends and customer pain points.

- Marketing Performance Tracking:
Integrating data from multiple sources, such as app store analytics, digital ad campaigns, and channel subscriptions (e.g., Telegram). This enabled the dashboard to monitor key metrics like ad engagement, app downloads, and subscriber growth.

- Data-Driven Insights:
The dashboard was connected to a PostgreSQL data warehouse, ensuring real-time data updates. This allowed the marketing and sales teams to quickly identify opportunities, troubleshoot issues, and make data-informed decisions to refine their strategies.

- Scalable and Responsive Design:
The dashboard was designed to be user-friendly and easily accessible, with a responsive layout that adapted well to different devices and screen sizes. This ensured the insights were readily available to the bank's stakeholders.


## Usage Instructions

1. Clone the repository:

   ```
   git clone https://github.com/Daniel-Andarge/AiML-marketing-analytics-dashboard.git
   cd AiML-marketing-analytics-dashboard
   ```

2. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Go to Kedro Pipeline folder

   ```
   cd kedro-pipeline
   ```

4. Run Jupyter Notebook

   ```
   jupyter notebook
   ```

5. You can now access the datasets view the data visualization.

## Exploratory Data Analysis (EDA)

### Sentiment analysis on Google app reviews

![EDA-sentiment](https://github.com/Daniel-Andarge/AiML-marketing-analytics-dashboard/blob/task-2/kedro-pipeline/notebooks/Sentiment.png)

### Sentiment - The App key strengths and weaknesses from Google app reviews

![EDA-key](https://github.com/Daniel-Andarge/AiML-marketing-analytics-dashboard/blob/main/kedro-pipeline/notebooks/output_46_0.png)

### Optimal Ad Placement on Tikvah-Ethiopia telegram channel

![EDA-view](https://github.com/Daniel-Andarge/AiML-marketing-analytics-dashboard/blob/task-2/kedro-pipeline/notebooks/ad_views.png)

To View the full EDA Click here [Exploratory-Data-Analysis](https://github.com/Daniel-Andarge/AiML-marketing-analytics-dashboard/blob/main/kedro-pipeline/notebooks/eda.png)

## Contributing Guidelines

Thank you for considering contributing to AiML-marketing-analytics-dashboard! I welcome contributions from everyone.

To contribute, follow these guidelines:

1. Fork the repository and create a new branch for your changes.
2. Check existing issues and pull requests to avoid duplicating work.
3. Follow the project's coding style and conventions.
4. Write clear commit messages and ensure your code is well-tested.
5. Provide a detailed description when submitting a pull request.
6. Be open to feedback and responsive during the review process.
7. Respect the project's code of conduct.
8. Your contributions will be licensed under the MIT License.

I appreciate your contributions!

## License

MIT License

AiML-marketing-analytics-dashboard

Copyright (c) 2024 Daniel Andarge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
