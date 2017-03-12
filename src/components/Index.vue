<template>
  <div class="container">
  <h1 v-if='error'>Error retrieving data</h1>
  <div class="input">
    <label>Name:</label>
    <input type='text' v-model="search">
    <input type='checkbox' id='indCheckbox' v-model='showIndividuals'>
    <label for='indCheckbox'>Individuals</label>  
    <input type='checkbox' id='entityCheckbox' v-model='showEntities'>
    <label for='entityCheckbox'>Entities</label>
  </div>
  <div class="table">
    <table v-if='showIndividuals'>
      <thead v-if='filteredIndividuals.length > 0'>
        <tr>
          <th class="ind-name">Name</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="individual in filteredIndividuals">
          <td>{{ individual.name }}</td>
          <td>{{ individual.details }}</td>
        </tr>
      </tbody>
    </table>
    <h3 v-if='filteredIndividuals.length ==0 && showIndividuals'>No matching individuals</h3>
    <div id="entity-table" v-if='showEntities'>
      <table>
        <thead v-if='filteredEntities.length > 0'>
          <tr>
            <th>Entity Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="entity in filteredEntities">
            <td>{{ entity.name }}</td>
          </tr>
        </tbody>
      </table>
      <h3 v-if='filteredEntities.length == 0'>No matching entities</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'index',
  data () {
    return {
      msg: 'LedgerX SDN Checker',
      individuals: [],
      entities: [],
      showIndividuals: true,
      showEntities: true,
      search: '',
      error: false,
    }
  },
  methods: {
    getSDNIndividuals: function() {
      this.$http.get('http://127.0.0.1:5000/individuals').then(response => {
        this.individuals = response.body;
        }, response => {
          this.error = true;
        }
      );
    },
    getSDNEntities: function() {
      this.$http.get('http://127.0.0.1:5000/entities').then(response => {
        this.entities = response.body;
        }, response => {
          this.error = true;
        }
      );
    }
  },
  computed: {
    filteredIndividuals: function() {
      return this.individuals.filter(individual => {
        return individual.name.indexOf(this.search.toUpperCase()) > -1
      })
    },
    filteredEntities: function() {
      return this.entities.filter(entity => {
        return entity.name.indexOf(this.search.toUpperCase()) > -1
      })
    },
    isInput: function() {
      return (this.search.length > 2);
    },
  },
  created: function() {
    this.getSDNIndividuals();
    this.getSDNEntities();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

th, td {
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

tr {
  height: 25px;
  vertical-align: top;
  line-height: 1.3em;
}

.ind-name {
  width: 30%;
}

.input {
  padding-bottom: 50px;
}

</style>
