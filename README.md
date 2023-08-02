# nagios_smartctl_test
This script (AI generated) supplements missing check in standard smartctl check of test results

nagios_smartctl reports disk as OK even if smartctl test is failed, this check is checking the test result itself, instead of overall device health, so you get notified when smartctl finds a failed disk
