/*print on the nuttShell
make px4fmu-v4_default
make px4fmu-v4_default upload
commands to run in nuttShell:
px4_simple_app
output:the accelerometer x,y,z  *10 READ
*/


#include <px4_config.h>
#include <px4_tasks.h>
#include <px4_posix.h>
#include <unistd.h>
#include <stdio.h>
#include <poll.h>
#include <string.h>

#include <uORB/uORB.h>
#include <uORB/topics/sensor_combined.h>
#include <uORB/topics/vehicle_attitude.h>


#define NUM_OF_READ 10
#define TIME_SEC 1000

__EXPORT int px4_simple_app_main(int argc, char *argv[]);

int px4_simple_app_main(int argc, char *argv[])
{

    int sensor = orb_subscribe(ORB_ID(sensor_combined));
    orb_set_interval(sensor, TIME_SEC);

    struct vehicle_attitude_s att;
	
    memset(&att, 0, sizeof(att));
    
	orb_advert_t att_pub = orb_advertise(ORB_ID(vehicle_attitude), &att);

    px4_pollfd_struct_t structSen[] = {
        { .fd = sensor,
		.events = POLLIN },
    };

    int error_counter = 0;

    for (int i = 0; i < NUM_OF_READ; i++) 
	{
	
        int poll_ret = px4_poll(structSen, 1, TIME_SEC);

        /* handle the poll result */
        if (poll_ret == 0)
		{
            PX4_ERR("[px4_simple_app] Got no data within a second");

        } else if (poll_ret < 0) 
		{
			PX4_ERR("[px4_simple_app] ERROR return value from poll(): %d", poll_ret);
            error_counter++;

        } else 
		{

            if (structSen[0].revents & POLLIN)
			{
                struct sensor_combined_s raw;
                /* copy sensors raw data into local buffer */
                orb_copy(ORB_ID(sensor_combined), sensor, &raw);
                PX4_WARN("[px4_simple_app] Accelerometer:\t%8.4f\t%8.4f\t%8.4f",
                       (double)raw.accelerometer_m_s2[0],
                       (double)raw.accelerometer_m_s2[1],
                       (double)raw.accelerometer_m_s2[2]);
            }

     
        }
    }

    return 0;
}