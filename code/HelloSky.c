
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
*/
__EXPORT int px4_simple_app_main(int argc, char *argv[]);

int px4_simple_app_main(int argc, char *argv[])
{
	printf("Hello Sky !!\n");
	return 0;
}