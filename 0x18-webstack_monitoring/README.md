
# Postmortem: E-commerce Checkout Outage
### Issue Summary
**Duration:**  
Friday, May 3rd, 2024, 14:12 PST - 15:37 PST (1 hour, 25 minutes)   
**Impact:**  
Our e-commerce checkout process experienced intermittent errors, preventing users from completing purchases. Approximately 30% of users attempting checkout were impacted, resulting in lost sales opportunities.  
**Root Cause:**  
A recent database configuration update to optimize query performance introduced an unintended side effect, causing deadlocks during peak checkout times.

### Timeline
- 14:12 PST: Monitoring alerts triggered, indicating a rise in failed checkout attempts.   
- 14:15 PST: On-call engineer investigates, confirming user reports of checkout errors. Initial suspicion falls on payment processing gateway due to similar issues in the past.   
- 14:20 PST - 14:45 PST: Investigation focuses on the payment gateway, including communication logs and test transactions. No anomalies are found.
- 14:45 PST: The investigation expands to the application server logs, revealing database connection timeouts coinciding with checkout spikes.
- 14:50 PST: The database team is engaged, and they begin analyzing recent configuration changes.
- 15:10 PST: A correlation is identified between the checkout outage and a database query optimization update implemented earlier that day.
- 15:20 PST: A rollback of the database configuration change is initiated.
- 15:30 PST: Monitoring confirms checkout functionality is restored.
- 15:37 PST: The incident is declared resolved, and a postmortem is scheduled.

### Root Cause and Resolution
The root cause of the outage was a recently deployed database configuration update aimed at improving query performance. While the update achieved its intended goal in most scenarios, it introduced deadlocks during peak checkout times when multiple user transactions attempted to modify the same data concurrently. Rolling back the configuration change resolved the issue and restored normal checkout functionality.

### Corrective and Preventative Measures
- Improved Code Review Process: The code review process for database schema changes and configuration updates will be reviewed to ensure a more thorough evaluation of potential side effects. This may involve including database administrators in the review process for relevant changes.
- Enhanced Monitoring: Monitoring will be expanded to include database lock timeouts and deadlocks. This will provide earlier detection of potential issues and allow for faster response times.
- Automated Testing: Automated testing will be implemented to simulate peak checkout loads and identify potential deadlocks before deployment.
- Standardized Rollback Procedures: A standardized procedure for quickly rolling back database configuration changes will be established to minimize downtime in case of unforeseen issues.
*** 
***  
     
This postmortem outlines the cause, resolution, and preventative measures for the recent e-commerce checkout outage. By implementing these changes, we aim to improve the stability and resilience of our e-commerce platform and minimize the impact of future incidents.
