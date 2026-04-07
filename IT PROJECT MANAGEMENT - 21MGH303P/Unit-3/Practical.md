# Practical 1: Project Performance Analysis

## Overview
This practical focuses on analyzing project performance using key metrics such as cost and schedule performance indices. It aligns with Unit-3 of the IT Project Management syllabus (Course Code: 21MGH303P), emphasizing monitoring techniques for cost, time, scope, and performance.

## Learning Objectives
- Understand how to calculate and interpret Cost Performance Index (CPI) and Schedule Performance Index (SPI).
- Analyze project performance to identify variances and recommend corrective actions.
- Apply project controlling techniques to maintain alignment with project goals.

## Prerequisites
- Basic knowledge of project scheduling (e.g., from Unit-2: PERT, CPM, Gantt Charts).
- Access to project management tools like Microsoft Project, Excel, or open-source alternatives (e.g., GanttProject).

## Required Tools/Materials
- Spreadsheet software (e.g., Microsoft Excel or Google Sheets).
- Sample project data (e.g., planned vs. actual costs and durations).

## Step-by-Step Procedure

1. **Gather Project Data**:
   - Collect data on planned value (PV), earned value (EV), and actual cost (AC) for key project tasks.
   - Example Dataset:
     | Task | Planned Value (PV) | Earned Value (EV) | Actual Cost (AC) | Planned Duration | Actual Duration |
     |------|---------------------|-------------------|------------------|------------------|-----------------|
     | Design | 10,000 | 8,000 | 12,000 | 5 days | 7 days |
     | Development | 20,000 | 15,000 | 18,000 | 10 days | 12 days |
     | Testing | 5,000 | 4,000 | 6,000 | 3 days | 4 days |

2. **Calculate Performance Indices**:
   - **Cost Performance Index (CPI)** = EV / AC
     - For Design: 8,000 / 12,000 = 0.67 (Under budget? No, over budget).
   - **Schedule Performance Index (SPI)** = EV / PV
     - For Design: 8,000 / 10,000 = 0.80 (Behind schedule).
   - Compute for all tasks and overall project.

3. **Analyze Variances**:
   - **Cost Variance (CV)** = EV - AC
   - **Schedule Variance (SV)** = EV - PV
   - Interpret: CPI > 1 indicates under budget; SPI > 1 indicates ahead of schedule.

4. **Visualize and Report**:
   - Create a Gantt chart or bar graph showing variances.
   - Generate a report: "The project is 20% over budget and 15% behind schedule. Recommend resource reallocation."

5. **Simulate Corrective Actions**:
   - Adjust resources in your tool and recalculate indices to observe improvements.

## Expected Outcomes
- A performance analysis report with calculations and charts.
- Insights into project health and mitigation strategies.

## Assessment Criteria
- Accuracy of calculations (40%).
- Quality of analysis and recommendations (30%).
- Visualization clarity (20%).
- Documentation (10%).

## References
- Syllabus Unit-3: "Analyzing cost and schedule performance index – Project performance analysis."
- Pressman, R. S. (2015). *Software Engineering: A Practitioner's Approach*.

---

*Save this content as `Practical_1_Project_Performance_Analysis.md` for reference.*

# Practical 2: Risk Management and Mitigation

## Overview
This practical introduces risk identification, analysis, and mitigation strategies in software projects. It draws from Unit-3 of the IT Project Management syllabus, focusing on project risk management and control techniques.

## Learning Objectives
- Identify potential risks in a software project.
- Assess risk probability and impact.
- Develop mitigation plans to minimize project disruptions.

## Prerequisites
- Familiarity with project phases (from Unit-1).
- Understanding of risk types (technical, schedule, cost).

## Required Tools/Materials
- Risk register template (Excel or Google Sheets).
- Brainstorming tools (e.g., MindMeister for risk mapping).

## Step-by-Step Procedure

1. **Identify Risks**:
   - For a sample software project (e.g., developing a web app), brainstorm risks.
   - Categories: Technical (e.g., integration failures), External (e.g., vendor delays), Internal (e.g., team skill gaps).
   - Example Risks:
     | Risk ID | Description | Category | Probability (Low/Med/High) | Impact (Low/Med/High) |
     |---------|-------------|----------|----------------------------|-----------------------|
     | R1 | Key developer leaves | Internal | Medium | High |
     | R2 | Scope creep from client | External | High | Medium |
     | R3 | Server outage during testing | Technical | Low | High |

2. **Analyze Risks**:
   - Calculate Risk Exposure = Probability × Impact (assign scores: Low=1, Med=3, High=5).
     - R1: 3 × 5 = 15 (High exposure).

3. **Develop Mitigation Strategies**:
   - For each risk: Avoidance, Transference, Mitigation, Acceptance.
     - R1 Mitigation: Cross-training team members; contingency plan for hiring.
     - R2: Implement change control process (from syllabus).

4. **Create Risk Register and Plan**:
   - Document in a table with triggers, owners, and monitoring frequency.
   - Simulate a risk event and apply mitigation.

5. **Review and Update**:
   - Discuss in a mock team meeting: How does this integrate with project monitoring?

## Expected Outcomes
- A populated risk register.
- A mitigation plan document outlining proactive steps.

## Assessment Criteria
- Comprehensiveness of risk identification (30%).
- Realistic analysis and scoring (30%).
- Feasibility of mitigation strategies (20%).
- Clear documentation (20%).

## References
- Syllabus Unit-3: "Project Risk Analysis - Project Risk management."
- Sommerville, I. (2010). *Software Engineering*.

---

*Save this content as `Practical_2_Risk_Management_and_Mitigation.md` for reference.*

# Practical 3: RMMM Plan Configuration Management, Software Configuration Management GitHub

## Overview
This practical covers the Risk Mitigation, Monitoring, and Management (RMMM) plan alongside Software Configuration Management (SCM) using GitHub. Based on Unit-3, it emphasizes configuration control and version management in projects.

## Learning Objectives
- Develop an RMMM plan to track and mitigate risks.
- Implement SCM practices using GitHub for version control.
- Understand how RMMM integrates with configuration management.

## Prerequisites
- Basic Git knowledge.
- Access to GitHub account.

## Required Tools/Materials
- GitHub repository (create a sample project repo).
- Git client (e.g., Git Bash or VS Code with Git integration).
- RMMM template (Word/Excel).

## Step-by-Step Procedure

1. **Develop RMMM Plan**:
   - Build on Practical 2 risks.
   - Structure: Risk (from register), Mitigation (actions), Monitoring (metrics/triggers), Management (escalation).
     - Example:
       | Risk | Mitigation | Monitoring | Management |
       |------|------------|------------|------------|
       | R1: Developer leaves | Cross-training | Weekly skill audits | Escalate to PM if score <80% |
   - Define review cadence (e.g., bi-weekly).

2. **Set Up SCM with GitHub**:
   - Create a new GitHub repo for a sample project (e.g., "SampleApp").
   - Initialize: `git init`, add files (e.g., README.md, code files).
   - Commit changes: `git add .`, `git commit -m "Initial commit"`, `git push origin main`.

3. **Integrate RMMM with SCM**:
   - Add RMMM plan as a Markdown file (e.g., RMMM.md) to the repo.
   - Simulate changes: Branch for risk mitigation (e.g., `git checkout -b risk-mitigation`), update code/docs, merge via Pull Request.
   - Track configurations: Use GitHub Issues for risk tracking.

4. **Practice Version Control**:
   - Create tags for milestones (e.g., `git tag v1.0`), resolve a "configuration drift" by reverting commits.
   - Collaborate: Invite a peer, review changes.

5. **Document and Audit**:
   - Generate a report: "SCM ensures traceable changes; RMMM file updated in commit #abc123."

## Expected Outcomes
- A GitHub repo with SCM setup and RMMM plan committed.
- Audit log of configuration changes tied to risks.

## Assessment Criteria
- Completeness of RMMM plan (30%).
- Proper GitHub SCM implementation (40%).
- Integration demonstration (20%).
- Repo documentation (10%).

## References
- Syllabus Unit-3: "RMMM plan and control - Software Configuration Management GitHub."
- Mall, R. (2014). *Fundamentals of Software Engineering*.

---

*Save this content as `Practical_3_RMMM_Plan_Configuration_Management_GitHub.md` for reference.*

# Practical 4: Unit Testing with Test Cases

## Overview
This practical involves creating and executing unit tests for software components, linking to project quality control from Unit-3. It ensures code reliability through systematic testing.

## Learning Objectives
- Design effective unit test cases.
- Implement and run tests using a framework.
- Analyze test results for defects and coverage.

## Prerequisites
- Basic programming knowledge (e.g., Python or Java).
- Understanding of testing strategies (from Unit-4 preview).

## Required Tools/Materials
- Programming IDE (e.g., PyCharm, Eclipse).
- Testing framework: pytest (Python) or JUnit (Java).
- Sample code module (e.g., a simple calculator function).

## Step-by-Step Procedure

1. **Prepare Test Environment**:
   - Write sample code, e.g., Python function:
     ```python
     def add(a, b):
         return a + b
     
     def divide(a, b):
         if b == 0:
             raise ValueError("Division by zero")
         return a / b
     ```

2. **Design Test Cases**:
   - Positive: add(2, 3) == 5
   - Negative: divide(10, 0) raises ValueError
   - Edge: add(0, 0) == 0; divide(1, 1) == 1.0
   - Use table:
     | Test Case ID | Description | Input | Expected Output | Type |
     |--------------|-------------|-------|-----------------|------|
     | TC1 | Valid addition | 2, 3 | 5 | Positive |
     | TC2 | Division by zero | 10, 0 | ValueError | Negative |

3. **Implement Tests**:
   - Using pytest (install if needed, but assume environment has it):
     ```python
     import pytest
     
     def test_add():
         assert add(2, 3) == 5
         assert add(0, 0) == 0
     
     def test_divide():
         assert divide(10, 2) == 5.0
         with pytest.raises(ValueError):
             divide(10, 0)
     ```
   - Run: `pytest -v`

4. **Execute and Analyze**:
   - Run tests, note pass/fail.
   - Calculate coverage (e.g., using pytest-cov: `pytest --cov`).
   - Debug failures and refactor code if needed.

5. **Report Results**:
   - Summary: "100% pass rate; 80% coverage. Recommend additional edge cases."

## Expected Outcomes
- Test suite code with execution logs.
- Coverage report and defect summary.

## Assessment Criteria
- Test case design thoroughness (30%).
- Implementation and execution accuracy (30%).
- Analysis depth (20%).
- Code quality and documentation (20%).

## References
- Syllabus Unit-3: "Unit testing with test cases."
- Pressman, R. S. (2015). *Software Engineering: A Practitioner's Approach* (Chapter on Testing).

---
