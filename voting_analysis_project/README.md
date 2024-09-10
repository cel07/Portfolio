# Voting Pattern Analysis

## Project Overview
This project focuses on analyzing the voting patterns of legislators using machine learning techniques such as clustering and dimensionality reduction. The goal is to identify voting behavior patterns and group legislators into clusters based on their similarity in voting behavior. Visualization techniques like t-SNE and dendrograms are used to gain deeper insights into the relationships between voting patterns and districts.

Voting patterns analysis is important for understanding the alignment of legislators on various issues, identifying potential voting blocs, and uncovering distinct voting behaviors across different districts.

## Motivation
Understanding voting patterns can help viewers, political analysts, and policymakers make informed decisions. Clustering legislators based on their voting behavior can provide insights into political alliances, differences between districts, and potential areas of consensus or disagreement. This project aims to explore the use of clustering and visualization techniques to provide a better understanding of how legislators vote and what drives their decisions.

## Dataset
The dataset used in this project is sourced from [LegiScan](https://legiscan.com/US/datasets). I selected the dataset for the year **2015-2016**, which contains detailed information about bills, roll call votes, legislators, and their voting records.

Key components of the dataset include:

 - **Bills**: Information about legislative bills being voted on.
 - **People**: Legislators' personal and demographic information, including their district and party affiliation.
 - **Roll Calls**: Records of roll call votes, indicating which legislator voted on which bill.
 - **Votes**: Detailed records of how each legislator voted (yea, nay, abstain, etc.).

The datasets are stored in the `data/` directory and include:
- `bills.csv`
- `people.csv`
- `rollcalls.csv`
- `votes.csv`

## Project Workflow
1. **Data Preprocessing**:
   - Load the dataset.
   - Merge the relevant data (bills, people, roll calls, and votes) to form a comprehensive view of voting patterns.
   - Clean and handle any missing values in the dataset.
2. **Exploratory Data Analysis (EDA)**:
   - Perform initial exploration of voting patterns and legislator characteristics.
   - Visualize voting distributions and patterns using heatmaps.
   - Identify similarities and differences across districts.
3. **Clustering Analysis**:
   - Apply K-Means clustering to group legislators based on their voting patterns.
   - Visualize the clusters using dimensionality reduction techniques like t-SNE.
4. **Hierarchical Clustering**:
   - Perform hierarchical clustering to explore the relationship between voting patterns across districts.
   - Visualize these relationships using dendrograms.
5. **Model Evaluation**:
   - Analyze the clustering results and the consistency of voting behaviors within each cluster.
   - Interpret the differences and similarities between clusters.
6. **Results**:
   - The analysis provides clear visualizations of voting clusters, district alignments, and the overall voting landscape of legislators. The t-SNE plot and dendrogram highlight distinct groups of legislators with similar voting patterns.

## Key Results
 - **Clustering**: K-Means clustering was used to group legislators into distinct clusters based on their voting behavior. The analysis revealed tight clusters where legislators have highly similar voting records, and other clusters with more variability.
 - **Dimensionality Reduction**: t-SNE effectively visualized the clusters in two-dimensional space, showing distinct groups of legislators with similar voting patterns.
 - **Hierarchical Clustering**: Dendrograms provided insight into how districts align in terms of voting similarity, showing the hierarchical relationships between districts based on their voting patterns.
 - **Key Insights**:
   - Certain districts showed strong internal cohesion in voting patterns, while others exhibited more varied behavior.
   - Clusters revealed patterns of alignment and opposition among legislators, potentially reflecting political or ideological divisions.

## Conclusion
This project successfully utilized clustering techniques and visualization to provide a clearer understanding of legislators' voting behaviors. The results offer valuable insights into political groupings and voting patterns that can be useful for further political analysis or policymaking.

## Visualizations
The project includes the following visualizations:
1. **Heatmap**: A heatmap that shows the average voting patterns within each cluster.
2. **t-SNE Plot**: A 2D visualization of legislators’ voting behavior after dimensionality reduction.
3. **Dendrogram**: A hierarchical clustering diagram showing the similarity of voting patterns between districts.

## Future Improvements
 - Explore additional clustering algorithms (e.g., DBSCAN or Agglomerative Clustering) to further refine voting pattern analysis.
 - Investigate how external factors (e.g., party affiliation, region) impact voting behavior and cluster formation.
 - Analyze the temporal trends of voting patterns over multiple legislative sessions.

## How to Run the Project
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/voting-pattern-analysis.git

