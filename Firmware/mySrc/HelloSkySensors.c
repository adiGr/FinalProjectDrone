
#include <px4_config.h>
#include <unistd.h>
#include <stdio.h>
#include <poll.h>
#include <string.h>

#include <uORB/uORB.h>
#include <uORB/topics/sensor_combined.h>
#include <uORB/topics/vehicle_attitude.h>


/*print "hello sky" on the nuttShell
make px4fmu-v4_default
make px4fmu-v4_default upload
commands to run in nuttShell:
px4_simple_app
output: Hello sky
print the accelerometer x,y,z
*/
__EXPORT int px4_simple_app_main(int argc, char *argv[]);

int px4_simple_app_main(int argc, char *argv[])
{
	printf("Hello Sky !!\n");
	
	px4_pollfd_struct_t fds[] = {
    { .fd = sensor_sub_fd,   .events = POLLIN },
	};
	while (true) {
    int poll_ret = px4_poll(fds, 1, 1000);

    if (fds[0].revents & POLLIN) {
        struct sensor_combined_s raw;
        /* copy sensors raw data into local buffer */
        orb_copy(ORB_ID(sensor_combined), sensor_sub_fd, &raw);
        printf("[px4_simple_app] Accelerometer:\t%8.4f\t%8.4f\t%8.4f\n",
                    (double)raw.accelerometer_m_s2[0],
                    (double)raw.accelerometer_m_s2[1],
                    (double)raw.accelerometer_m_s2[2]);
    }
	return 0;
}