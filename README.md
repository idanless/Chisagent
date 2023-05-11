<h1>Chisagent</h1>

<p>The goal of this project is to address an issue commonly encountered in Linux systems, where monitoring the audit syslog and EDR may generate false alarms when kernel syscall commands are executed. This project aims to fix this issue by only capturing the real user commands from the system's profile, and sending them to the SOC (Security Operations Center). This will enable the SOC team to be 100% sure if the commands were executed by a real user, or if they were triggered by a service or a cron job. This simple fix can help mitigate security risks and improve system security.</p>

<p>This project is intended as a proof-of-concept and can be modified and adapted as needed.</p>

<h2>Screenshots</h2>

<img src="screenshot1.png" alt="Screenshot 1">
<p>Caption for screenshot 1.</p>

<img src="screenshot2.png" alt="Screenshot 2">
<p>Caption for screenshot 2.</p>

<h2>Installation</h2>

<p>To install this project, follow these steps:</p>

<ol>
  <li>copy Chisagent.py to the server</li>
  <li>edit the /etc/bash.bashrc by vi or nano</li>
  <li>add this line in the end of the file export PROMPT_COMMAND='python3 /home/demo/Chisagent/Chisagent.py "$(history 1 | sed -e "s/^[ ]*[0-9]\+[ ]*//g")"' (note:change this path /home/demo/Chisagent/Chisagent.py )</li>
</ol>

<p>After completing these steps, the project should be installed and ready to use. shuld see under /tmp history json</p>
