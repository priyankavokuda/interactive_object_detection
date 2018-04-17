#%% Parameters


######Train parameters######
# patch size in format (y, x)

min_samples_per_split = 20
max_depth = 15
n_splits = 2000
#The number of thresholds to evaluate per feature
n_thresholds = 10
ratios = (1.,) #(0.5, 0.75, 1., 1.25, 1.5)
#How many patches from each image
n_samples_pos = 50#2
n_samples_neg = 50#2
n_feature_channels = 15
max_patches_per_node = 40000

######Test parameters######

n_threads = 1
min_prob_threshold = 0.5
#test_offset = 1
application_step_size = 2
use_reduced_grid = False
test_offset = 0
#n_pos = 228
n_pos = 50

eps = 1e-10/2
num_samples = 1000

##### Interaction#####
interactive = False

train_image_dir = 'train_images'
train_annot_dir = 'train_boundingboxes'
test_image_dir = 'test_images'
test_annot_dir = 'test_boundingboxes'
eval_image_dir = 'eval_images'
eval_annot_dir = 'eval_boundingboxes'
exp_dir = 'exp_images'
annot_dir = 'BoundingBoxes'
fertilized_sys_path = '/home/priyanka/Documents/autonomous_systems/master_thesis/code/fertilized-forests/build/bindings/python'
deep_features_path = '/home/priyanka/Documents/autonomous_systems/master_thesis/code/tensorflow-vgg-master-d22cc94cb66517b054eec8c92f5b4db6ad517fc5/'
forest_name = 'forest.pkl'
feat_name = 'feat_images.pkl'

feature_type = 2# 1. rgb,2. hog, 3. deep
 #1 -synthetic, 2:HILA, 3:NASH, 4:Weizmann_horse 6:VOC
dataset_flag = 7

# print('dataset_flag',dataset_flag)
if dataset_flag ==1:
    patch_size = (16, 16)
    n_trees = 15
    root_dir = r'/home/priyanka/Documents/autonomous_systems/master_thesis/code/synthetic/'
    n_samples_pos = 50  # 2
    n_samples_neg = 50  # 2
    extension = '.png'
    n_detec = 8
    scales = (0.7,) #(0.7, 0.6, 0.5, 0.4, 0.3)
    clear_area = 120
    iou = 0.5
    experiments = 5

if dataset_flag==2:
    patch_size = (15, 15)
    n_trees = 15
    root_dir = r'/home/priyanka/Documents/autonomous_systems/master_thesis/code/HILA/'
    extension = '.png'
    n_samples_pos = 200  # 2
    n_samples_neg = 200  # 2
    n_detec = 19
    scales = (1.8,1.4,1,0.8) #(0.7, 0.6, 0.5, 0.4, 0.3)
    clear_area = 80
    all_image_dir = 'all_images'
    iou = 0.25
    experiments = 3

if dataset_flag==3:
    patch_size = (16, 16)
    n_trees = 15
    root_dir = r'/home/priyanka/Documents/autonomous_systems/master_thesis/code/NASH/'
    extension = '.jpg'
    n_samples_pos = 200  # 2
    n_samples_neg = 200  # 2
    n_detec = 20
    #in descending
    scales = (0.75,1.0) #(0.7, 0.6, 0.5, 0.4, 0.3)
    clear_area = 50
    all_image_dir = 'all_images'
    iou = 0.45
    experiments = 5

if dataset_flag==4:
    patch_size = (16, 16)
    n_trees = 15
    root_dir = r'/home/priyanka/Documents/autonomous_systems/master_thesis/code/WeizmannMultiScale/'
    extension = '.png'
    n_samples_pos = 25  # 2
    n_samples_neg = 25  # 2
    n_detec = 1
    #in descending
#    scales = (1.0,) #(0.7, 0.6, 0.5, 0.4, 0.3)
    scales = (1.0,0.75)
#    scales = (1.0,0.85,0.75)
#    scales = (1.0,0.95,0.85,0.75)
    
    clear_area = 200
    all_image_dir = 'all_images'
    iou = 0.5
    experiments = 10

if dataset_flag==5:
    patch_size = (10, 10)
    n_trees = 5
    root_dir = r'/home/priyanka/Documents/autonomous_systems/master_thesis/code/NASH_app/'
    extension = '.jpg'
    n_samples_pos = 20  # 2
    n_samples_neg = 20  # 2
    n_detec = 15
    #in descending
    scales = (0.75,1.0) #(0.7, 0.6, 0.5, 0.4, 0.3)
    clear_area = 50
    all_image_dir = 'all_images'
    iou = 0.45
    experiments = 5

if dataset_flag==6:
    patch_size = (16, 16)
    n_trees = 15
    root_dir = r'/home/priyanka/Documents/autonomous_systems/master_thesis/code/VOC/'
    extension = '.jpg'
    n_samples_pos = 100  # 2
    n_samples_neg = 100  # 2
    n_detec = 3
    #in descending
    scales = (0.75,0.5,0.25,0.20) #(0.7, 0.6, 0.5, 0.4, 0.3)
    clear_area = 200
    all_image_dir = 'all_images'
    iou = 0.3
    experiments = 5


if dataset_flag==7:
    patch_size = (16, 16)
    n_trees = 15
    root_dir = r'/home/priyanka/Documents/autonomous_systems/master_thesis/code/leaf/'
    extension = '.png'
    n_samples_pos = 25  # 2
    n_samples_neg = 25  # 2
    n_detec = 12
    #in descending
#    scales = (1.0,) #(0.7, 0.6, 0.5, 0.4, 0.3)
    scales = (0.75,1.0) 
    clear_area = 200
    all_image_dir = 'all_images'
    iou = 0.45
    experiments = 5
#    scales = (1.0,0.85,0.75)
#    scales = (1.0,0.95,0.85,0.75)