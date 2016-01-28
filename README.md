
#### How to install the plugin

1. Get the plugin script from the public repository by using wget to get the raw file contents, and set the file to be executable.
    ```
    cd /usr/lib/rackspace_monitoring_agent/plugins/
    wget https://raw.githubusercontent.com/oldarmyc/monitor_plugins/master/mounted_filesystem.py
    chmod +x /usr/lib/rackspace-monitoring-agent/plugins/mounted_filesystem.py
    ```

2. Restart the monitoring daemon

    init.d
    ```
    /etc/init.d/rackspace-monitoring-agent restart
    ```

    upstart
    ```
    service rackspace-monitoring-agent restart
    ```

    systemd
    ```
    systemctl restart rackspace-monitoring-agent.service
    ```

3. Login to Cloud Intelligence portal https://intelligence.rackspace.com, or you can go through the Cloud Control Panel by going to Servers - Rackspace Intelligence

4. Create a check for the server you want to monitor using the following values.

    * Check Type: Custom Plugin
    * Check Name: Name the check to whatever makes sense i.e. Mounted FS Check
    * Command: mounted_filesystem.py PATH-MOUNT-POINT

      For example if a CBS volume is mounted at /mnt the command would be the following:

      ```
      mounted_filesystem.py /mnt
      ```

    * Timeout: 5000


5. Create the alarm for the check that you just created using the following values. Make sure to click Next Step on the first screen.

    Alarm Name: Custom name for the alarm
    Notification Plan: Who to notify in case of an alert
    Alarm Criteria:
    ```
    if (metric['writestatus'] != 'RW') {
        return new AlarmStatus(CRITICAL, 'Filesystem is: #{writestatus}');
    }
    ```

You can update the parameters of the check i.e. check period and timeout after the creation of the check.
