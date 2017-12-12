import sys

def getJarName(artifact):
    jar = artifact[artifact.index("android-all"):]
    jar = jar.replace(":", "-")
    jar = jar + ".jar"
    return jar

# def f(name, artifact):
#     jar = getJarName(artifact)
#     print "%s=%s/jar/%s" % (artifact.replace(":", "\\:"), name, jar)

def getKey(jar):
    key = "org.robolectric\:android-all\:"
    # print "jar in call: " + jar
    version = jar.split("/")[3].strip()[12:-4]
    # print "version: " + version
    key = key + version
    return key

def getValue(jar):
    return "../" + jar[jar.index("org_robolectric"):]

def main(argv):
    # print argv
    # with open("external/robolectric/tmp.properties") as f:
    #     all_jars = f.read().split(" ")

    # # f = open("tmp_outputfile", "w")
    for jar in argv[1:]:
        # print "jar from before calls: " + jar
        key = getKey(jar)
        # print "after get key"
        value = getValue(jar)
        # print "after get value"
        print ("%s=%s" % (key, value))
        # f.write("%s=%s\n" % (key, value))
    # f.close()

if __name__ == "__main__":
    print "hello"
    main(sys.argv)

# f(
#     name = "org_robolectric_android_all_8_1_0_robolectric_r4402310",
#     artifact = "org.robolectric:android-all:8.1.0-robolectric-r4402310",
# )

# f(
#     name = "org_robolectric_android_all_8_0_0_r4_robolectric_r1",
#     artifact = "org.robolectric:android-all:8.0.0_r4-robolectric-r1",
# )

# f(
#     name = "org_robolectric_android_all_7_1_0_r7_robolectric_r1",
#     artifact = "org.robolectric:android-all:7.1.0_r7-robolectric-r1",
# )

# f(
#     name = "org_robolectric_android_all_7_0_0_r1_robolectric_r1",
#     artifact = "org.robolectric:android-all:7.0.0_r1-robolectric-r1",
# )

# f(
#     name = "org_robolectric_android_all_6_0_1_r3_robolectric_r1",
#     artifact = "org.robolectric:android-all:6.0.1_r3-robolectric-r1",
# )

# f(
#     name = "org_robolectric_android_all_5_1_1_r9_robolectric_r2",
#     artifact = "org.robolectric:android-all:5.1.1_r9-robolectric-r2",
# )

# f(
#     name = "org_robolectric_android_all_5_0_2_r3_robolectric_r0",
#     artifact = "org.robolectric:android-all:5.0.2_r3-robolectric-r0",
# )

# f(
#     name = "org_robolectric_android_all_4_4_r1_robolectric_r2",
#     artifact = "org.robolectric:android-all:4.4_r1-robolectric-r2",
# )

# f(
#     name = "org_robolectric_android_all_4_3_r2_robolectric_r1",
#     artifact = "org.robolectric:android-all:4.3_r2-robolectric-r1",
# )

# f(
#     name = "org_robolectric_android_all_4_2_2_r1_2_robolectric_r1",
#     artifact = "org.robolectric:android-all:4.2.2_r1.2-robolectric-r1",
# )

# f(
#     name = "org_robolectric_android_all_4_1_2_r1_robolectric_r1",
#     artifact = "org.robolectric:android-all:4.1.2_r1-robolectric-r1",
# )

# f(
#     name = "org_robolectric_android_all_8_1_0_robolectric_4402310",
#     artifact = "org.robolectric:android-all:8.1.0-robolectric-4402310",
# )

# f(
#     name = "org_robolectric_android_all_8_0_0_r4_robolectric_0",
#     artifact = "org.robolectric:android-all:8.0.0_r4-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_o_preview_4_robolectric_0",
#     artifact = "org.robolectric:android-all:o-preview-4-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_o_preview_2_robolectric_0",
#     artifact = "org.robolectric:android-all:o-preview-2-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_o_preview_1_robolectric_0",
#     artifact = "org.robolectric:android-all:o-preview-1-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_6_0_1_r3_robolectric_0",
#     artifact = "org.robolectric:android-all:6.0.1_r3-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_7_1_0_r7_robolectric_0",
#     artifact = "org.robolectric:android-all:7.1.0_r7-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_7_0_0_r1_robolectric_0",
#     artifact = "org.robolectric:android-all:7.0.0_r1-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_6_0_0_r1_robolectric_0",
#     artifact = "org.robolectric:android-all:6.0.0_r1-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_5_1_1_r9_robolectric_1",
#     artifact = "org.robolectric:android-all:5.1.1_r9-robolectric-1",
# )

# f(
#     name = "org_robolectric_android_all_5_1_1_r9_robolectric_0",
#     artifact = "org.robolectric:android-all:5.1.1_r9-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_4_4_r1_robolectric_1",
#     artifact = "org.robolectric:android-all:4.4_r1-robolectric-1",
# )

# f(
#     name = "org_robolectric_android_all_5_0_0_r2_robolectric_1",
#     artifact = "org.robolectric:android-all:5.0.0_r2-robolectric-1",
# )

# f(
#     name = "org_robolectric_android_all_5_0_0_r2_robolectric_0",
#     artifact = "org.robolectric:android-all:5.0.0_r2-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_4_4_r1_robolectric_0",
#     artifact = "org.robolectric:android-all:4.4_r1-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_4_2_2_r1_2_robolectric_0",
#     artifact = "org.robolectric:android-all:4.2.2_r1.2-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_4_3_r2_robolectric_0",
#     artifact = "org.robolectric:android-all:4.3_r2-robolectric-0",
# )

# f(
#     name = "org_robolectric_android_all_4_1_2_r1_robolectric_0",
#     artifact = "org.robolectric:android-all:4.1.2_r1-robolectric-0",
# )
